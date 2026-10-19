# A prime-field zero-mode transition in three-tap affine convolution

## Finding
Let \(q=p^r\ge 3\) be a prime power, let \(a\) generate \(\mathbb F_q^\times\), and choose \(b\in\mathbb F_q^\times\), \(c\in\mathbb F_q\). Write \(G=\operatorname{AGL}(1,q)\), with group multiplication \((u,v)(s,t)=(us,v+ut)\), and consider the three *distinct* affine transformations
\[
S=\{(1,0),(1,b),(a,c)\}.
\]
For the unweighted left-convolution operator \(T_S=\sum_{s\in S}L_s\) on \(\mathbb C[G]\), where \((L_sf)(g)=f(s^{-1}g)\), the **exact integer determinant** is
\[
\det T_S=
\begin{cases}
(2^{q-1}-1)\bigl(2^{p^{r-1}-1}-1\bigr)^{q-1},&p\text{ odd},\\
2^{q-1}+1,&p=2.
\end{cases}
\]
Moreover, its complex kernel has exactly the dimension
\[
\dim_{\mathbb C}\ker T_S=
\begin{cases}q-1,&p\text{ odd and }r=1,\\0,&\text{otherwise}.\end{cases}
\]
Thus this canonical three-tap filter is singular **exactly over odd prime fields**, never over proper finite-field extensions. In particular, for every prime \(p\equiv2\pmod3\), the group \(\operatorname{AGL}(1,p)\) has order \(p(p-1)\), not divisible by three, yet its three-distinct-tap convolution has nullity \(p-1\). There are infinitely many such primes.

## Assumptions and scope
The result concerns convolution by the specified unweighted support, not every three-element subset of \(G\). The multiplier \(a\) must be primitive, \(b\ne0\), and \(q\ge3\); in characteristic two this requires \(q\ge4\). No symmetry of the support under inversion is assumed, so this is a generally nonselfadjoint operator and its Cayley representation may have loops. Determinants and kernels are over \(\mathbb C\) with the standard delta-function basis; no normalization by \(|G|\) is used.

## Proof
**1. The irreducible Fourier sectors.** The affine action of \(G\) on \(\mathbb F_q\) is sharply two-transitive. Consequently the \(q\)-dimensional complex permutation module splits as \(\mathbf1\oplus V\), where \(V\) is irreducible of dimension \(q-1\): two-transitivity makes the permutation-character self-inner-product equal to two. Independently, the quotient \(G/(\mathbb F_q,+)\cong\mathbb F_q^\times\) contributes \(q-1\) distinct one-dimensional characters. Since
\[
(q-1)\cdot1^2+(q-1)^2=q(q-1)=|G|,
\]
these are all the complex irreducibles. Thus the regular convolution determinant equals the product of its \(q-1\) scalar character values times the determinant on \(V\) raised to the \((q-1)\)-st power. Corresponding kernel dimensions are added with the same representation multiplicities.

**2. Eliminate the auxiliary parameters.** Conjugating \(S\) by a translation replaces \((a,c)\) with \((a,0)\), because \(a\ne1\), while fixing \((1,b)\). Subsequent conjugation by a nonzero scalar sends \((1,b)\) to \((1,1)\) and leaves \((a,0)\) fixed. Such conjugations act by permutation similarities on \(T_S\). It suffices to calculate for \(S=\{(1,0),(1,1),(a,0)\}\). The calculation below also works directly with an arbitrary nonzero \(b\).

**3. The nonlinear block.** Fix a nontrivial additive character \(\psi\) of \(\mathbb F_q\) and the Fourier basis \(e_t(x)=\psi(tx)\), \(t\in\mathbb F_q\), for functions on the affine line. The constant vector \(e_0\) forms the trivial submodule, and the remaining \(q-1\) Fourier vectors span \(V\). A translation acts diagonally with entry \(\psi(-bt)\), while multiplication by \(a\) permutes the nonzero frequencies through a single cycle of length \(q-1\). Hence the nonlinear block is a cyclic shift plus a diagonal matrix with entries \(d_t=1+\psi(-bt)\). For a cyclic shift \(P\) of length \(n\ge2\), direct determinant expansion gives
\[
\det(\operatorname{diag}(d_1,\ldots,d_n)+P)
=\prod_{j=1}^n d_j+(-1)^{n-1}.
\]
The only contributing permutations are the identity and the full cycle. Thus, with \(n=q-1\),
\[
\det(T_S|_V)=\prod_{t\in\mathbb F_q^\times}(1+\psi(t))+(-1)^{q-2}.
\]
Here \(\{-bt:t\ne0\}=\mathbb F_q^\times\), so \(b\) is immaterial.

If \(p\) is odd, put \(m=p^{r-1}\). Among nonzero \(t\), the character value \(1\) occurs \(m-1\) times and every other \(p\)-th root of unity occurs \(m\) times. Since
\[
\prod_{j=1}^{p-1}(1+\zeta_p^j)=\Phi_p(-1)=1
\quad(p\text{ odd}),
\]
the product is \(2^{m-1}\). Now \(q-1\) is even, so
\[
\boxed{\det(T_S|_V)=2^{p^{r-1}-1}-1.}
\]
If \(p=2\), some nonzero \(t\) has \(\psi(t)=-1\). The product vanishes, whereas \(q-1\) is odd, giving \(\boxed{\det(T_S|_V)=1}\).

**4. Scalar sectors and the full determinant.** Every one-dimensional character is trivial on translations and takes the multiplier \(a\) to some \((q-1)\)-st root of unity \(\xi\). Its value on the three taps sums to \(2+\xi\), which is nonzero because \(|\xi|=1\). Their product is
\[
\prod_{\xi^{q-1}=1}(2+\xi)=2^{q-1}-(-1)^{q-1}.
\]
Multiplication by the \((q-1)\)-st power of the nonlinear determinant gives the claimed full determinant in both characteristics.

**5. Exact nullity and arithmetic contrast.** In odd prime characteristic with \(r=1\), the nonlinear block determinant vanishes. All diagonal coefficients \(1+\psi(-bt)\) are nonzero because an odd-order root of unity cannot equal \(-1\). The cyclic linear equations recursively determine every component from one initial component, so the nonlinear kernel has dimension at most one; its zero determinant makes the dimension exactly one. Its multiplicity in the regular module is \(q-1\). In every other case the nonlinear determinant is nonzero and the scalar determinants never vanish. This proves the exact nullity.

For \(p\equiv2\pmod3\), neither \(p\) nor \(p-1\) is divisible by three. Infinitely many such primes exist: were their product \(P\) finite, the positive integer \(3P-1\equiv2\pmod3\) would have a prime divisor congruent to two modulo three but dividing none of the factors of \(P\).

## Verification
The included standalone `CHECK.py` builds the affine permutation representation and, for selected orders, the complete group-regular convolution matrices directly from finite-field arithmetic. It uses exact Bareiss determinants, exact modular determinants and modular ranks, without floating-point computations. Execution of `python3 CHECK.py` returned `PASS: 42 checks on q = 3,4,5,7,8,9,11.` The cases of orders four, eight and nine explicitly exercise extension fields. The unrestricted prime-power theorem depends on the preceding character-count and Fourier-block proof, not on these finite calculations.

## Relationship to prior work
General factorization of Cayley adjacency characteristic polynomials into irreducible representation blocks is established in M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs* (2013), especially Corollary 7. The present claim does not assert novelty for Fourier decomposition or for the standard affine-group character degrees; it supplies the particular cyclotomic determinant, exact nullity, and prime-field versus extension-field threshold for the specified three-tap filters. A later thesis by A. S. A. Al-Tarimshawy, *Singular Graphs* (2018), treats a six-element inverse-symmetric connection set on \(\operatorname{AGL}(1,5)\), not the present three-element (identity-containing, generally directed) filter. Related three-tap results on generalized dihedral and dicyclic groups address index-two inversion extensions, not these full affine multiplier groups.

## Limitations
The theorem does not classify all three-tap supports on affine groups, all subgroup multipliers, weighted taps, nonprime-power translation groups, graph adjacency matrices without loops, or nonzero eigenvalues. Numerical verification covers only listed fields; the exact determinant and all-degree statements follow analytically. Earlier implicit instances of the same cyclotomic product or affine representation computation could affect publication priority.

## References
- M. Arezoomand and B. Taeri, *On the Characteristic Polynomial of n-Cayley Digraphs*, Electronic Journal of Combinatorics **20** (2013), #P57, published 2013-10-07, DOI: 10.37236/3105, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p57/pdf/ .
- A. S. A. Al-Tarimshawy, *Singular Graphs*, University of East Anglia doctoral thesis (2018), Chapter 4, https://ueaeprints.uea.ac.uk/id/eprint/68916/1/PhD_thesis_%282%29.pdf .
