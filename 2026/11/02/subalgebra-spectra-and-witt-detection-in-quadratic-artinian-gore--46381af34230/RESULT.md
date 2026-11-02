# Subalgebra spectra and Witt detection in quadratic Artinian Gorenstein algebras

## Finding
Let \(q\) be an odd prime power, \(d\ge 2\), and \(B\) a nonsingular symmetric bilinear form on \(V=\mathbb F_q^d\). Define the commutative unital algebra
\[
A_B=\mathbb F_q1\oplus V\oplus\mathbb F_q z,\qquad vw=B(v,w)z,\quad vz=z^2=0.
\]
Its maximal ideal \(\mathfrak m=V\oplus\mathbb F_qz\) satisfies \(\mathfrak m^2=\mathbb F_qz\) and \(\mathfrak m^3=0\); nonsingularity makes \(\mathbb F_qz\) its socle. Let \(P_B(t)=\sum_S t^{\dim_{\mathbb F_q}S}\), summed over all unital \(\mathbb F_q\)-subalgebras \(S\subseteq A_B\). Put \({d\brack k}_q=\prod_{i=0}^{k-1}(q^{d-i}-1)/(q^{k-i}-1)\), and let \(I_{d,k}(B)\) be the number of totally \(B\)-isotropic \(k\)-subspaces of \(V\). Then
\[
\boxed{P_B(t)=\sum_{k=0}^d{d\brack k}_q t^{k+2}+\sum_{k=0}^{w(B)}q^k I_{d,k}(B)t^{k+1}.}
\]
Here \(w(B)\) is the Witt index, and the isotropic numbers are completely explicit. For odd \(d=2m+1\),
\[
I_{2m+1,k}={m\brack k}_q\prod_{i=0}^{k-1}(q^{m-i}+1),\qquad 0\le k\le m.
\]
For even \(d=2m\), hyperbolic (split) and elliptic (nonsplit) types have, respectively,
\[
I^+_{2m,k}={m\brack k}_q\prod_{i=0}^{k-1}(q^{m-1-i}+1),\quad 0\le k\le m,
\]
\[
I^-_{2m,k}={m-1\brack k}_q\prod_{i=0}^{k-1}(q^{m-i}+1),\quad 0\le k\le m-1.
\]
Empty products equal one and all unlisted isotropic counts equal zero. The dimension-two coefficient distinguishes the two even-dimensional Witt types by the exact gap
\[
\boxed{[t^2]P_{B_+}(t)-[t^2]P_{B_-}(t)=2q^m.}
\]
There is also a distributional dichotomy. At fixed odd \(q\), if \(S_d\) is uniformly selected among these unital subalgebras for any nonsingular sequence \(B_d\), then
\[
\boxed{\Pr(\mathbb F_qz\not\subseteq S_d)=q^{-d^2/12+d/6+O_q(1)}.}
\]
In probability, \(\dim S_d/d\to1/2\); conditional on \(\mathbb F_qz\not\subseteq S_d\), instead \(\dim S_d/d\to1/3\). The typical dimension has a discrete-Gaussian centered limit: for \(d=2m\), \(\Pr(\dim S_d=m+2+j)\to q^{-j^2}/\sum_{\ell\in\mathbb Z}q^{-\ell^2}\), and for \(d=2m+1\), \(\Pr(\dim S_d=m+2+j)\to q^{j-j^2}/\sum_{\ell\in\mathbb Z}q^{\ell-\ell^2}\), for each fixed integer \(j\). These formulas are independent of the higher-dimensional choice of nonsingular form except for the explicitly detected Witt type.

## Assumptions and scope
All subalgebras contain \(1\), are closed under \(\mathbb F_q\)-scalar multiplication, and are counted as distinct embedded subspaces (not isomorphism types). The base field has odd characteristic. The multiplication is associative: products of any two elements of \(\mathfrak m\) lie in the annihilating line \(\mathbb F_qz\), so all triple products in \(\mathfrak m\) vanish. The symbols \(+\) and \(-\) refer to the two similarity classes of even-dimensional nonsingular symmetric forms. The result holds for all odd prime powers, including non-prime fields. In the probability statements, \(q\) is fixed and \(d\) tends to infinity, with either Witt type permitted in even dimensions.

## Proof
**1. Complete subalgebra normal form.** Given a unital \(S\), subtract scalar multiples of \(1\) from every element to write \(S=\mathbb F_q1\oplus W\), where \(W\le V\oplus\mathbb F_qz\). If \(z\in W\), then \(W=U\oplus\mathbb F_qz\) for a unique \(U\le V\), since subtracting the central coordinate of any lift leaves an element of \(W\). Every such \(W\) is product-closed, giving \({d\brack k}_q\) choices when \(\dim U=k\), with \(\dim S=k+2\).

If \(z\notin W\), projection \(V\oplus\mathbb F_qz\to V\) restricts to a linear isomorphism from \(W\) onto a subspace \(U\le V\). Consequently \(W=\{u+\phi(u)z:u\in U\}\) for a unique linear map \(\phi:U\to\mathbb F_q\). For \(u,v\in U\), the product of their lifts is \(B(u,v)z\), which lies in \(W\) if and only if \(B(u,v)=0\) because \(W\cap\mathbb F_qz=0\). Thus product closure is equivalent to \(B|_{U\times U}=0\). For each totally isotropic \(U\) of dimension \(k\), there are exactly \(q^k\) choices of \(\phi\), and \(\dim S=k+1\). This proves the stated generating polynomial with no missing or multiply counted cases.

**2. Isotropic subspace numbers.** Write \([r]_q=(q^r-1)/(q-1)\). The number of isotropic projective lines in nondegenerate orthogonal spaces of dimensions \(2r+1\), split \(2r\), and nonsplit \(2r\) is, respectively,
\[
L_{2r+1}=[2r]_q,\quad L^+_{2r}=(q^{r-1}+1)[r]_q,\quad L^-_{2r}=(q^{r-1}-1)[r]_q.
\]
These formulas follow by counting zeros of a standard diagonal/hyperbolic quadratic form. In odd characteristic, \(B(v,v)=0\) is the equivalent condition for an isotropic line, and a totally isotropic subspace has the inherited orthogonal quotient \(U^\perp/U\). A \(k\)-dimensional totally isotropic \(U\) has \(L_{d-2k}\) distinct isotropic \((k+1)\)-dimensional extensions, indexed by isotropic lines of that quotient; **there is no extra factor for selecting a lift**. Conversely a \((k+1)\)-space has \([k+1]_q\) hyperplanes of dimension \(k\). Hence \(I_{d,0}=1\) and
\[
I_{d,k+1}=I_{d,k}\frac{L_{d-2k}}{[k+1]_q},
\]
where the quotient retains the original parity and split type. Substituting the three line-count formulas and telescoping gives exactly the three products in the finding. In dimension \(2m\), the line counts at dimension \(2\) yield
\[
I^+_{2m,1}-I^-_{2m,1}=2q^{m-1}.
\]
The \(t^2\) coefficient is \(1+qI_{d,1}\), proving the exact gap \(2q^m\).

**3. Large-dimension concentration.** Fix \(q\). Define \(G_d=\sum_k{d\brack k}_q\), the number of subalgebras containing \(z\), and \(H_d=\sum_kq^k I_{d,k}\), the number avoiding it. Set \(C_q=\prod_{j\ge1}(1-q^{-j})^{-1}<\infty\). The Gaussian-binomial product gives
\[
q^{k(d-k)}\le{d\brack k}_q\le C_q q^{k(d-k)}.
\]
It follows, by completing the square and summing a uniformly summable discrete Gaussian, that \(G_d=q^{d^2/4+O_q(1)}\).

For every applicable Witt type, the displayed isotropic product, after extracting powers of \(q\), has the form
\[
I_{d,k}=q^{kd-3k^2/2-k/2}\,c_{d,k}(q),\qquad 1\le c_{d,k}(q)\le C'_q,
\]
where \(C'_q\) is a finite constant depending only on \(q\). The lower and upper bounds follow from the same Gaussian-binomial inequality and the finite products \(\prod(1+q^{-j})\). Thus
\[
q^kI_{d,k}=q^{kd-3k^2/2+k/2+O_q(1)}
=q^{(d+1/2)^2/6-\tfrac32(k-(d+1/2)/3)^2+O_q(1)}.
\]
The maximizing integer is within a bounded distance of \((d+1/2)/3\), which lies strictly below the Witt-index cutoff for all sufficiently large \(d\). Summation again gives \(H_d=q^{d^2/6+d/6+O_q(1)}\). Consequently \(H_d/(G_d+H_d)=q^{-d^2/12+d/6+O_q(1)}\). The same quadratic tails imply \(\dim S_d/d\to1/3\) conditioned on omitting \(z\). The containing class dominates and has \(\dim S_d/d\to1/2\).

Finally, for \(d=2m\), \({2m\brack m+j}_q/q^{m^2-j^2}\to C_q\) for each fixed \(j\), and these terms are dominated by \(C_q q^{-j^2}\). For \(d=2m+1\), the corresponding exponent relative to \(m(m+1)\) is \(j-j^2\). Dominated convergence yields the two discrete-Gaussian limits. The omitted-socle mass tends to zero, so the limits hold without conditioning.

## Verification
The accompanying dependency-free `verify.py` computes RREF bases of every subspace of the actual nilpotent ideal for selected finite fields and dimensions. It tests closure directly by multiplying the basis vectors using the bilinear form, independently of the predicted polynomial; it also directly enumerates totally isotropic subspaces and checks the even-dimensional Witt gap. Successful exhaustive cases: \(q=3\), \(d=2,3,4,5\), both even-dimensional types; \(q=5\), \(d=2,3,4\), both types in dimension two. In particular, for \(q=3,d=4\), the split and nonsplit dimension distributions are \((1,49,112,130,40,1)\) and \((1,31,40,130,40,1)\) at dimensions \(1,\ldots,6\). Their dimension-two gap is \(18=2\cdot3^2\). The verifier also checks the gap symbolically in sample parameters \(q=3,5,7,11\), \(d=2,4,6,8\). The asymptotic statements are proved algebraically, not by finite extrapolation.

To reproduce, run `python3 verify.py` beside this document; it finishes with `VERIFY_OK`. The verifier tests prime fields directly, whereas the general proof covers every odd prime power.

## Relationship to prior work
The Artinian Gorenstein condition and Hilbert vector \((1,d,1)\) are standard, as is the classification of nonsingular quadratic spaces and the classical formulas for totally isotropic subspaces. Bezerra, Gondim, Ilardi, and Zappalà study Gorenstein Hilbert functions and Perazzo algebras; their 2022 source motivates the socle/Hilbert-function setting but does not give this subalgebra polynomial or the associated probability laws. Jelisiejew's local Gorenstein classification treats isomorphism types of short algebras, not the embedded finite-field subalgebra count and its growing-dimensional measure. Neither algebraic normal form nor finite orthogonal polar-space counting alone is presented as a new general result: the contribution is the complete subalgebra spectrum, its Witt-type detector, and the sharply quantified conditional rare-event dimension dichotomy for this specific infinite family.

An earlier study of subalgebra enumeration in finite nilpotent alternative algebras by Strade is relevant but its complete text could not be inspected; it is a genuine residual literature-priority risk, particularly for the exact enumerator. The growing-dimensional probabilistic conclusions have not been compared to a full-text theorem from that source. Absence of search hits does not certify novelty.

## Limitations
The theorem assumes nonsingular symmetric \(B\) in odd characteristic; degeneracy and characteristic two alter the structure. It counts embedded unital \(\mathbb F_q\)-linear subalgebras, not all subrings or their isomorphism classes. The discrete-Gaussian limits hold only for fixed \(q\), and do not assert quantitative finite-\(d\) total-variation error bounds. Independent verification and independent publication-priority review have not been performed.

## References
1. L. Bezerra, R. Gondim, G. Ilardi, and G. Zappalà, *On minimal Gorenstein Hilbert function*, arXiv:2206.05572, first version 11 June 2022, https://arxiv.org/abs/2206.05572.
2. J. Jelisiejew, *Classifying local Artinian Gorenstein algebras*, arXiv:1511.08007 (2015), https://arxiv.org/abs/1511.08007.
3. H. Strade, *Enumeration results in nilpotent algebras*, Proc. Amer. Math. Soc. 49 (1975), 20–24, doi:10.1090/S0002-9939-1975-0357526-4. Full text unavailable during this review.
4. Standard finite orthogonal-geometry isotropic-line and Witt-decomposition formulas; explicit identities and derivation are provided in the proof rather than assumed as a new theorem.
