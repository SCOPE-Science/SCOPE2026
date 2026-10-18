# Complete subquandle size distribution for rank-one unipotent Alexander quandles

## Finding

Let \(p\) be any prime, \(f\ge1\), and \(q=p^f\). On \(Q=\mathbb F_q^2\) define
\[
(a,b)\triangleright(c,d)=(a+b-d,b).
\]
This is the nonconnected Alexander quandle with linear automorphism \(T=I+N\), where \(N(a,b)=(b,0)\), \(N^2=0\), and \(N\ne0\). A **subquandle** means a nonempty subset closed under the binary operation, which in this finite setting is also closed under each restricted inverse right translation.

For each such subquandle \(S\), set
\[
B=\{b\in\mathbb F_q:\exists a\ (a,b)\in S\},\qquad
S_b=\{a\in\mathbb F_q:(a,b)\in S\},
\]
and let \(W=\operatorname{span}_{\mathbb F_p}\{b-d:b,d\in B\}\). Then **all** subquandles are obtained uniquely by choosing a nonempty \(B\subseteq\mathbb F_q\), forming \(W\) as above, and, independently for every \(b\in B\), choosing a nonempty union of additive \(W\)-cosets for \(S_b\). No restriction couples the choices for different \(b\).

Write \({n\brack k}_p\) for the Gaussian binomial coefficient (zero outside \(0\le k\le n\)). Define, for integers \(0\le t\le f\) and \(1\le j\le p^t\),
\[
a_{t,j}(p)=\sum_{u=0}^{t}(-1)^{t-u}
 p^{\binom{t-u}{2}+t-u}{t\brack u}_p\binom{p^u}{j},
\]
where ordinary binomial coefficients vanish when the bottom argument exceeds the top. In particular \(a_{t,j}(p)\) is a nonnegative integer: it counts the \(j\)-subsets of a fixed affine \(t\)-flat whose smallest affine span is that flat.

The complete **embedded-subquandle cardinality generating polynomial** is
\[
\boxed{
\mathcal S_{p,f}(z)=\sum_{\substack{\varnothing\ne S\subseteq Q\\ S\text{ subquandle}}}z^{|S|}
=\sum_{t=0}^{f}p^{f-t}{f\brack t}_p
 \sum_{j=1}^{p^t}a_{t,j}(p)
 \left((1+z^{p^t})^{p^{f-t}}-1\right)^j.
}
\]
Every coefficient is an exact count. The result applies equally in characteristic two; it is not a quotient by an automorphism group or an isomorphism-type count.

For a prime field \(f=1\), the polynomial simplifies to
\[
\boxed{\mathcal S_{p,1}(z)=p((1+z)^p-1)+\sum_{j=2}^{p}\binom pj z^{pj}.}
\]
In particular \(\mathcal S_{2,1}(1)=7\), \(\mathcal S_{3,1}(1)=25\), \(\mathcal S_{5,1}(1)=181\), whereas \(\mathcal S_{2,2}(1)=119\) and \(\mathcal S_{3,2}(1)=10933\). The coefficient of \(z^{q^2}\) is always one.

## Assumptions and scope

The underlying additive group of \(\mathbb F_q\) is considered as an \(f\)-dimensional vector space over \(\mathbb F_p\). Multiplication in \(\mathbb F_q\) is not used in the quandle operation, so the classification and polynomial depend only on \((p,f)\). A nonempty subset \(B\) has a unique smallest affine \(\mathbb F_p\)-flat \(b_0+W\); its dimension \(t\) lies between zero and \(f\). Every nonempty fiber contains at least one point. Subquandles are individually counted as actual subsets of the \(q^2\)-point quandle.

## Proof

**1. Alexander property and finite closure.** The map \(T(a,b)=(a+b,b)\) has inverse \(T^{-1}(a,b)=(a-b,b)\), and the usual affine formula \(x\triangleright y=Tx+(I-T)y\) gives the displayed operation. Hence it is a quandle. A finite nonempty subset closed under each right translation inherits a permutation from the restriction of every such bijection: injectivity on the subset implies surjectivity. Thus its inverse right translations also preserve the subset.

**2. Fiber description: necessity.** Fix a subquandle \(S\) and its nonempty base support \(B\). For every \(b,d\in B\), every \(a\in S_b\), and any \(c\in S_d\), closure gives
\[
(a,b)\triangleright(c,d)=(a+b-d,b)\in S,
\]
so \(S_b+(b-d)\subseteq S_b\). Translation by a fixed field element has finite order. Repeatedly applying this inclusion therefore gives equality. The same argument with sums and additive inverses shows \(S_b+w=S_b\) for all \(w\in W\). Consequently \(S_b\) is a union of additive \(W\)-cosets. It must be nonempty by the definition of \(B\).

**3. Fiber description: sufficiency and uniqueness.** Conversely, choose arbitrary nonempty \(B\), construct \(W\) from its differences, and choose independently one nonempty union of \(W\)-cosets for each \(b\in B\). Because \(b-d\in W\), the formula above preserves the first-coordinate fiber for every pair of elements. Closure follows. The base projection and fibers are uniquely recovered from \(S\), so this construction does not identify distinct choices.

**4. Exact affine-span coefficients.** Fix an affine \(t\)-flat \(L\) in the \(\mathbb F_p\)-affine space \(\mathbb F_q\). For any affine subflat \(U\subseteq L\) of dimension \(u\), there are \(\binom{p^u}{j}\) subsets of cardinality \(j\) contained in \(U\). The interval from \(U\) to \(L\) in the affine-flat poset is isomorphic to an interval of the linear-subspace lattice of codimension \(t-u\). Its Möbius function is \((-1)^{t-u}p^{\binom{t-u}{2}}\). There are exactly \(p^{t-u}{t\brack u}_p\) affine \(u\)-flats inside \(L\). Möbius inversion on the affine-span containment relation therefore yields exactly \(a_{t,j}(p)\) \(j\)-subsets whose smallest affine span is \(L\).

**5. Weight of the fibers.** A dimension-\(t\) \(\mathbb F_p\)-subspace \(W\) has \(p^t\) elements and index \(p^{f-t}\) in \(\mathbb F_q\). The size enumerator for one nonempty union of \(W\)-cosets is exactly
\[
 F_t(z)=\sum_{\ell=1}^{p^{f-t}}\binom{p^{f-t}}\ell z^{\ell p^t}
 =(1+z^{p^t})^{p^{f-t}}-1.
\]
For a base support with \(j\) elements, choices in its \(j\) separate fibers give \(F_t(z)^j\). There are \(p^{f-t}{f\brack t}_p\) affine \(t\)-flats in the ambient \(f\)-space. Summing their spans and the possible support cardinalities gives precisely the asserted formula, without overcounting.

**6. Prime-field simplification and extremal coefficient.** If \(f=1\), a singleton base support has \(W=0\), and its nonempty vertical fiber may be any subset of \(p\) elements, contributing \(p((1+z)^p-1)\). Every base support of size at least two spans the entire additive field, so each selected base coordinate forces its full \(p\)-element fiber, contributing the remaining sum. The only subquandle of size \(q^2\) is \(Q\) itself.

## Verification

The accompanying standalone standard-Python script `verify.py` forms the complete operation table independently from the formula and exhaustively tests every nonempty subset for closure when \((p,f)=(2,1),(3,1),(2,2)\), corresponding to ambient sizes \(4,9,16\). Its direct size-distribution counters agree with the theorem:

- \((2,1)\): \(4z+2z^2+z^4\), total \(7\).
- \((3,1)\): \(9z+9z^2+3z^3+3z^6+z^9\), total \(25\).
- \((2,2)\): \(16z+24z^2+16z^3+28z^4+24z^6+6z^8+4z^{12}+z^{16}\), total \(119\).

The script also checks Gaussian-Möbius span coefficients and the partition identity for support-subset counts at further parameters. It prints `ALL_UNIPOTENT_SUBQUANDLE_CHECKS_PASSED`. Finite test cases are not used to infer the universal theorem, which is established by the preceding argument.

## Relationship to prior work

Iijima–Murao, *On connected component decompositions of quandles* (2017, arXiv:1704.07689), studies connected components of Alexander quandles. The present \(T=I+N\) has nontrivial fixed-coordinate projection, and the fibers permit many unions of cosets, not merely connected components. Their component decomposition does not supply the complete embedded-subquandle size polynomial.

Amsberry–Bergquist–Horstkamp–Lee–Yetter, *Complementation of Subquandles* (2023, arXiv:2304.09747), studies complementation properties in subquandle lattices. Those results do not explicitly determine the cardinality enumerator above. Higashitani–Kurihara, *Generalized Alexander quandles of finite groups and their characterizations* (2022, arXiv:2210.16763), examines generalized Alexander-quandle structure rather than enumerating the entire subquandle lattice of this unipotent family.

The novel statement assessed here is the complete fiber-wise parametrization **together with** the all-field cardinality polynomial. It does not claim that the elementary affine-subspace Möbius formula, Alexander-quandle construction, or connected-component decomposition was unknown previously.

## Limitations

The classification is for the single rank-one nilpotent operator \(N\) of Jordan type \((2)\) over \(\mathbb F_q\), not arbitrary nilpotent Jordan types, arbitrary finite Alexander quandles, or subquandle isomorphism types. The size polynomial does not classify automorphism orbits or count subquandle complements. No claim of exhaustive historical priority is made: an equivalent all-subquandle formula may exist under another terminology for affine racks, subracks, or finite module extensions. The direct checks are limited to small ambient sets; the universal proof is deductive.

## References

1. Y. Iijima and T. Murao, *On connected component decompositions of quandles*, arXiv:1704.07689 (2017). https://arxiv.org/abs/1704.07689
2. A. Amsberry, K. Bergquist, S. Horstkamp, J. Lee and D. N. Yetter, *Complementation of Subquandles*, arXiv:2304.09747 (2023). https://arxiv.org/abs/2304.09747
3. R. Higashitani and H. Kurihara, *Generalized Alexander quandles of finite groups and their characterizations*, arXiv:2210.16763 (2022). https://arxiv.org/abs/2210.16763
