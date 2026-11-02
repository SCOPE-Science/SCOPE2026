# Uniform dyadic Waring-length laws for even powers

## Finding

Fix any **even integer** \(k\ge4\). Put \(s=\nu_2(k)\), \(m=s+2\), and \(B=2^m\). For integers \(n\ge1\) and \(0\le t\le B\), let
\[
A_{k,t}(n)=\#\{a\in\mathbb Z/2^n\mathbb Z: a\equiv x_1^k+\cdots+x_t^k\pmod{2^n}\text{ for some }x_1,\ldots,x_t\},
\]
where zero summands are allowed and \(A_{k,0}(n)=1\).

**Exact finite-modulus census.** For every \(1\le t<B\) and \(n\ge1\),
\[
A_{k,t}(n)=\begin{cases}
\min\{t+1,2^n\},&1\le n\le m,\\
t2^{n-m}+1,&m<n\le k,\\
t2^{n-m}+A_{k,t}(n-k),&n>k.
\end{cases}
\]
In particular \(A_{k,B}(n)=2^n\) for all \(n\ge1\). The recurrence admits an explicit closed form. With \(r=1+((n-1)\bmod k)\) and
\[
c_{k,t}=\frac{t}{B(1-2^{-k})},
\]
one has, for every \(n\ge1\),
\[
\boxed{A_{k,t}(n)=c_{k,t}2^n+A_{k,t}(r)-c_{k,t}2^r.}
\]
Consequently the remainder after subtracting \(c_{k,t}2^n\) is **exactly periodic in \(n\) with period dividing \(k\)**; in particular it is bounded for fixed \(k,t\).

**Pointwise \(2\)-adic length.** For \(a\in\mathbb Z_2\), let \(L_k(a)\) be the least number of \(k\)-th powers in \(\mathbb Z_2\) summing to \(a\), with \(L_k(0)=0\). For nonzero \(a\), put
\[
j=\left\lfloor\frac{\nu_2(a)}k\right\rfloor,\qquad u=2^{-kj}a\in\mathbb Z_2,
\]
and let \(\rho\in\{0,1,\ldots,B-1\}\) represent \(u\pmod B\). Then
\[
\boxed{L_k(a)=\begin{cases}\rho,&1\le\rho<B,\\B,&\rho=0.\end{cases}}
\]
Thus the maximal \(2\)-adic length is \(15\) when \(k=4\), and \(B\) when \(k\ge6\) is even. These **maximum values were established previously**; the new statement is the entire length distribution and the uniform finite-modulus census above.

**Complete length distribution.** For Haar-uniform \(a\in\mathbb Z_2\),
\[
\boxed{\Pr(L_k(a)=t)=\frac{2^k}{B(2^k-1)}\quad(1\le t<B),}
\]
while
\[
\boxed{\Pr(L_k(a)=B)=\frac{2^k-B}{B(2^k-1)},\qquad\Pr(L_k(a)=0)=0.}
\]
For \(k=4\), all lengths \(1,\ldots,15\) therefore have frequency \(1/15\). For \(k=6\), lengths \(1,\ldots,7\) each have frequency \(8/63\), and length \(8\) has frequency \(1/9\). The finite-ring length frequencies equal \(2^{-n}(A_{k,t}(n)-A_{k,t-1}(n))\) for \(t<B\) and \(1-2^{-n}A_{k,B-1}(n)\) for \(t=B\), taking \(A_{k,0}(n)=1\). Thus their errors from the limiting probabilities are \(O_{k,t}(2^{-n})\).

## Assumptions and scope

All sums are taken in the indicated commutative ring. A representation by \(t\) summands allows zero among the variables, so it is equivalent to representation by at most \(t\) nonzero summands. The exponent \(k\) is **any fixed even integer at least four**, not necessarily a power of two; \(n,t\) range over the stated integers. Dividing an element of \(\mathbb Z_2\) by \(2^{kj}\) is used only when its valuation is at least \(kj\). Haar measure on \(\mathbb Z_2\) is the probability measure assigning mass \(2^{-h}\) to each residue class modulo \(2^h\). No claim is made for other local primes or for odd exponents.

## Proof

**1. Exact unit-power image.** The multiplicative group of odd \(2\)-adic integers decomposes as \(\mathbb Z_2^\times\cong\{\pm1\}\times(1+4\mathbb Z_2)\). The \(2\)-adic logarithm identifies \(1+4\mathbb Z_2\) with the additive group \(4\mathbb Z_2\). Since \(k\) is even and \(\nu_2(k)=s\), the image of the \(k\)-th power map is exactly
\[
(\mathbb Z_2^\times)^k=1+2^{s+2}\mathbb Z_2=1+B\mathbb Z_2.
\]
This standard structural ingredient also appears in the proof of Theorem 6.11 of Kowalczyk--Miska (arXiv:2206.09904). Even bases have \(k\)-th powers in \(2^k\mathbb Z_2\). Notice \(m\le k\) for all even \(k\ge4\).

**2. The disjoint odd/even decomposition.** Take \(1\le t<B\). If a sum of \(t\) \(k\)-th powers contains exactly \(h\) odd bases, then its residue modulo \(B\) equals \(h\), since each odd power is \(1\pmod B\) and each even power is \(0\pmod B\). Thus \(1\le h\le t\) gives one of the pairwise disjoint residue classes \(h+B\mathbb Z_2\). Conversely, **every element** of the class \(h+B\mathbb Z_2\) is a sum of exactly \(h\) odd \(k\)-th powers: write it as \((h-1)\cdot1^k+z\) with \(z\in1+B\mathbb Z_2\), then extract an odd \(k\)-th root of \(z\). Pad with zero powers if needed. For an element congruent to zero modulo \(B\), the odd-base count must be a multiple of \(B\); as it is strictly below \(B\), it is zero. Consequently
\[
\{\text{sums of at most }t\text{ powers}\}
=\left(\bigcup_{h=1}^{t}(h+B\mathbb Z_2)\right)
\,\dot\cup\,2^k\{\text{sums of at most }t\text{ powers}\}.
\]
The union is disjoint because the first part has nonzero residue modulo \(B\), whereas \(2^k\) is divisible by \(B\). The identity holds both in \(\mathbb Z_2\) and in its finite quotients, with the obvious interpretation of multiplication by \(2^k\).

**3. Finite-modulus counting.** For \(n\le m\), odd powers are \(1\) and even powers \(0\pmod{2^n}\). Hence the represented residues are exactly the images of \(0,1,\ldots,t\) modulo \(2^n\), giving \(\min\{t+1,2^n\}\). If \(m<n\le k\), each nonzero residue class \(h\pmod B\) gives \(2^{n-m}\) residues, and the all-even part gives just zero, hence \(t2^{n-m}+1\). If \(n>k\), the \(t\) nonzero classes contribute \(t2^{n-m}\) elements; multiplication by \(2^k\) maps residues modulo \(2^{n-k}\) injectively to divisible residues modulo \(2^n\). Therefore the all-even branch contributes exactly \(A_{k,t}(n-k)\). When \(t=B\), the \(B\) odd-summand counts from \(1\) through \(B\) cover all classes modulo \(B\), and each lifts fully; thus every residue is representable.

**4. Closed form and the finite discrepancy.** For fixed \(t<B\), set \(c=c_{k,t}\). The recurrence for \(n>k\) gives
\[
A_{k,t}(n)-c2^n=A_{k,t}(n-k)-c2^{n-k},
\]
because \(c(2^k-1)2^{n-k}=t2^{n-m}\). Repeatedly subtracting \(k\) from \(n\) ends at \(r=1+((n-1)\bmod k)\), which proves the displayed closed form and its periodic bounded error.

**5. Pointwise length and the limiting law.** For a nonzero \(a\in\mathbb Z_2\), repeatedly remove blocks of \(k\) powers of two from \(a\) until its valuation becomes less than \(k\). Because a representation of length strictly below \(B\) in the zero class modulo \(B\) uses only even bases, dividing the representation by \(2^k\) preserves its length. Conversely any representation of the quotient can be multiplied by \(2^k\). This forces the minimum below \(B\) to be invariant under the stripping. The residual element \(u\) with \(\nu_2(u)<k\) either has nonzero residue \(\rho\pmod B\), in which case the disjoint decomposition proves that its minimal length is exactly \(\rho\), or has residue zero, in which case no representation using fewer than \(B\) powers exists. The universal bound \(B\) proves the latter minimum is \(B\). If \(k=4\), the zero-residue case is impossible for \(u\), since \(B=2^k\).

For \(t<B\), the set \(\{a:L_k(a)\le t\}\) is the disjoint union, over \(j\ge0\), of \(2^{kj}(\bigcup_{h=1}^{t}(h+B\mathbb Z_2))\). The Haar measure of the \(j\)-th layer is \(t\,2^{-kj}/B\), so geometric summation gives
\[
\Pr(L_k\le t)=\frac{t}{B}\sum_{j=0}^{\infty}2^{-kj}
=\frac{t}{B(1-2^{-k})}.
\]
Successive differences give equal probabilities for lengths \(1,\ldots,B-1\); the remaining probability belongs to length \(B\), while the singleton zero has measure zero. Dividing the exact finite count by \(2^n\) gives the stated effective convergence rates. This completes the proof.

## Verification

A dependency-free Python program, `verify.py`, directly computes \(k\)-th-power residue images modulo \(2^n\) via cyclic bitset convolution, without using the decomposition or the recurrence to construct those images. It compares the resulting cardinalities against the theorem for every \(1\le n\le12\), each even \(k\in\{4,6,8,10,12,14\}\), and all \(1\le t\le B\), totaling **1,056 equality checks**. The expected cardinalities use the symbolic recurrence; the actual cardinalities are exhaustive for each finite ring. A second check compares the \(k=4\) case with all applicable formulas in Arias--Borja--Anaya Proposition 32, for \(1\le n\le30\) and \(3\le t\le15\), totaling **390 exact comparisons**. Running `python3 verify.py` should print `VERIFY_OK` and `PUBLISHED_FORMULA_COMPATIBILITY_OK`. The infinite and uniform-in-\(k\) claims depend on the proof, not on extrapolation from these finite tests.

## Relationship to prior work

Kowalczyk and Miska, *On Waring numbers of henselian rings* (arXiv:2206.09904, first publicly posted June 20, 2022), prove in Theorem 6.11 the **maximum** even-exponent Waring lengths over \(\mathbb Z_2\) and identify the kth powers of odd units. Their proof supplies a basic subgroup fact reused here, but does not state the distribution across individual lengths or the exact count for every smaller summand budget and finite dyadic modulus.

Arias, Borja, and Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n* (2023), provide general lifting/counting methods (notably Propositions 4 and 8), a two-summand sixth-power example (Proposition 26), and, in Proposition 32, an exact special case for **fourth powers** and \(3\le t\le15\). That special case is **already known and not claimed as novel**. The present work extends the exact census to **every even exponent \(k\ge4\)** with a single formula and supplies the corresponding complete \(2\)-adic probability law. Neither the maximum-only theorem nor the published fourth-power table states that uniform generalization. These older results are essential antecedents; the derivation is deliberately elementary given their structure.

C. Small's *Waring's Problem Mod n* (1977) is a relevant older source for the extremal modular Waring problem. Its complete text was not available in this study; no assertion is made about uninspected results beyond the portions summarized or cited in the accessible primary literature.

## Limitations

The statement is local to the prime two and to even exponents at least four. It does not compute global modular Waring constants or integer Waring numbers, nor representation multiplicities. The exact maximum and the fourth-power counting case are pre-existing results. The all-even-exponent finite-modulus distribution is a direct development of the known unit-power image; this close dependence carries a genuine originality risk if an older equivalent closed distribution is located. The complete 1977 Small paper was not available for inspection. Independent external verification has not been performed.

## References

1. T. Kowalczyk and P. Miska, *On Waring numbers of henselian rings*, arXiv:2206.09904 (first public version June 20, 2022), Theorem 6.11 and its proof. https://arxiv.org/abs/2206.09904
2. F. Arias, J. Borja, and S. Anaya, *Counting Integers Representable as Sums of k-th Powers Modulo n*, Journal of Integer Sequences **26** (2023), Article 23.8.1 (published August 28, 2023), Section 7 and Propositions 4, 8, 31--32. https://cs.uwaterloo.ca/journals/JIS/VOL26/Borja/borja4.pdf
3. C. Small, *Waring's Problem Mod n*, American Mathematical Monthly **84** (1977), 12--25, DOI: 10.1080/00029890.1977.11994269. Metadata and secondary references consulted; full text not inspected.
