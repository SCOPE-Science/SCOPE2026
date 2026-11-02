# Exponential scarcity of simultaneous left-and-right transversals on two-row rectangular bands

## Finding
Let \(I\) and \(J\) be nonempty finite sets, let \(S=I\times J\), and equip \(S\) with the rectangular-band product
\[
(i,j)(k,\ell)=(i,\ell).
\]
Call a permutation \(\alpha\in\operatorname{Sym}(S)\) *two-sided complete* when **both** \(x\mapsto x\alpha(x)\) and \(x\mapsto\alpha(x)x\) are permutations of \(S\). This asks for the same permutation to provide a transversal in the given multiplication table and in its opposite table. It must not be confused with the different *strong complete mapping* definition in the cited source.

**Theorem.** If \(\min(|I|,|J|)=2\) and \(r=\max(|I|,|J|)\ge1\), the exact number of two-sided complete permutations is
\[
B_r=r!(r+1)!.
\]
The number of ordinary (one-sided) complete permutations is
\[
L_r=2^r(r!)^2,
\]
so the exact fraction of one-sided complete permutations which are two-sided is
\[
\frac{B_r}{L_r}=\frac{r+1}{2^r}.
\]
It decreases to zero exponentially as \(r\to\infty\), despite the existence of a two-sided complete permutation for every \(r\). For \(r=2,3,4\) the pair \((L_r,B_r)\) is respectively \((16,12)\), \((288,144)\), \((9216,2880)\).

**Refinement.** For \(|I|=2\), fix the two row permutations \(p,q\in\operatorname{Sym}(J)\) occurring in the second coordinate of \(\alpha\). The number of two-sided complete permutations with these prescribed second-coordinate maps is exactly \(2^{c(q^{-1}p)}\), where \(c(\rho)\) denotes the number of cycles (including fixed points) of a permutation \(\rho\).

## Assumptions and scope
A rectangular band is a semigroup with the displayed product; labels are fixed and permutations are counted as set maps, not modulo semigroup isomorphism. A *one-sided* complete mapping is a bijection \(\alpha\) for which \(x\mapsto x\alpha(x)\) is bijective. Two-sided completeness is an additional property of the **same** \(\alpha\), stronger than separate existence of a left- and a right-complete mapping. The theorem is valid for every integer \(r\ge1\). The case \(|J|=2\) follows from the same counting argument applied to the opposite rectangular band, which exchanges the two products.

## Proof
By exchanging factors and reversing multiplication if necessary, take \(I=\{0,1\}\) and \(J=\{1,\dots,r\}\). Write
\[
\alpha(i,j)=(a_i(j),b_i(j)),\qquad a_i(j)\in\{0,1\},\quad b_i(j)\in J.
\]
Left completeness means that \((i,j)\mapsto(i,b_i(j))\) is bijective. Hence \(p=b_0\) and \(q=b_1\) must independently be permutations of \(J\). Right completeness means that \((i,j)\mapsto(a_i(j),j)\) is bijective. Since \(|I|=2\), this is equivalent to
\[
a_0(j)=\varepsilon_j,\qquad a_1(j)=1-\varepsilon_j
\]
for a bit \(\varepsilon_j\in\{0,1\}\) at each column \(j\).

We now impose the requirement that \(\alpha\) itself be bijective. For a given target second coordinate \(t\in J\), the two input cells with second output coordinate \(t\) are \((0,p^{-1}(t))\) and \((1,q^{-1}(t))\). Their first output coordinates are respectively \(\varepsilon_{p^{-1}(t)}\) and \(1-\varepsilon_{q^{-1}(t)}\). They are distinct if and only if
\[
\varepsilon_{p^{-1}(t)}=\varepsilon_{q^{-1}(t)}.
\]
As \(t\) varies, this says that the binary labelling \(\varepsilon:J\to\{0,1\}\) is constant on every cycle of \(q^{-1}p\) (equivalently of \(p^{-1}q\)). For fixed \(p,q\), the number of admissible labellings is exactly \(2^{c(q^{-1}p)}\), proving the refinement and giving a bijective parametrization of every required \(\alpha\).

Each fixed \(\rho=q^{-1}p\) arises from exactly \(r!\) ordered pairs \((p,q)\). Thus
\[
B_r=r!\sum_{\rho\in\operatorname{Sym}(J)}2^{c(\rho)}.
\]
For an indeterminate \(z\), put \(F_r(z)=\sum_{\rho\in S_r}z^{c(\rho)}\). Inserting the new letter \(r\) into a permutation of \(r-1\) letters either creates a singleton cycle, contributing a factor \(z\), or inserts into one of \(r-1\) existing cycle positions, leaving the cycle count unchanged. Therefore \(F_0(z)=1\) and \(F_r(z)=(z+r-1)F_{r-1}(z)\), so \(F_r(2)=2\cdot3\cdots(r+1)=(r+1)!\). Consequently \(B_r=r!(r+1)!\).

To count one-sided complete mappings, select arbitrary row permutations \(p,q\), giving \((r!)^2\) choices. At each target column \(t\), the two input cells having second output coordinate \(t\) must be assigned the two distinct first output coordinates in some order. These \(r\) choices are independent, with two choices each; every resulting mapping is bijective. Hence \(L_r=2^r(r!)^2\). Dividing proves the fraction, and \((r+1)/2^r\to0\). This completes the proof.

## Verification
The dependency-free checker `verify.py` uses the product \((i,j)(k,\ell)=(i,\ell)\) directly and exhaustively enumerates every permutation of the \(2r\)-element set for \(r=1,2,3,4\); it tests bijectivity of both product maps independently. It separately enumerates the row-permutation/bit parametrization through \(r=4\) and computes the cycle enumerator through \(r=7\). Running `python verify.py` produced `VERIFY_OK` with direct counts \((2,2)\), \((16,12)\), \((288,144)\), \((9216,2880)\). These are finite checks, not a substitute for the all-\(r\) proof above.

## Relationship to prior work
Araújo, Bentz, Cameron, Hendrey, and Kinyon, *Complete Mappings of Semigroups* (arXiv:2608.25092v1, publicly posted 25 August 2026), define complete mappings, prove in Proposition 1.3 the equivalence of **existence** of left- and right-handed complete mappings (not necessarily the same permutation), and discuss rectangular bands in Section 12. Section 13 studies *strong complete mappings*, meaning permutations which are both complete mappings and orthomorphisms; this is **not** the simultaneous left/right condition here. The new theorem determines the exact count for one permutation satisfying both handedness conditions and the exponential scarcity inside all one-sided maps. Neither Proposition 1.3 nor the cited Sections 12–13 give this formula in the inspected primary text. The factor-specific cycle-parametrization is a structural refinement of the mere existence statement.

## Limitations
The closed form concerns rectangular bands having a factor of cardinality two; no general formula for arbitrary \(|I|,|J|\ge3\) is established. The word *two-sided* is a definition stated here, not a claim that it coincides with any author's term *strong complete mapping*. The formula counts labelled permutations, not orbits under band automorphisms. Broad or older enumeration of constrained permutation arrays might subsume this count; historical priority is not independently certified.

## References
1. J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, and M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1 (25 August 2026), especially Proposition 1.3 and Sections 12–13. https://arxiv.org/abs/2608.25092
2. P. J. Cameron, *Complete mappings of semigroups*, research note (27 August 2026). https://cameroncounts.wordpress.com/ (post of this date; conceptual context only).
