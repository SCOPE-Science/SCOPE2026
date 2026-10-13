# Finite-field forms of cyclic permutation evolution algebras
## Finding
Let \(q\) be a prime power and \(m\ge2\). For \(\mathbf c=(c_0,\ldots,c_{m-1})\in(\mathbb F_q^\times)^m\), define the evolution algebra \(E(\mathbf c)\) by
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=c_i e_{i+1},
\]
with indices modulo \(m\). Set
\[
N=2^m-1,\qquad
\Theta(\mathbf c)=\prod_{i=0}^{m-1}c_i^{2^{m-1-i}},\qquad
g=\gcd(N,q-1).
\]
Then
\[
E(\mathbf c)\cong E(\mathbf d)
\quad\Longleftrightarrow\quad
[\Theta(\mathbf c)]=[\Theta(\mathbf d)]^{2^k}
\]
in \(\mathbb F_q^\times/(\mathbb F_q^\times)^N\) for some \(0\le k<m\). The quotient is cyclic of order \(g\), and cyclic rotation of the directed support acts on it by doubling. Consequently the exact number of isomorphism classes in this full weighted-cycle family is
\[
I_m(q)=\frac1m\sum_{k=0}^{m-1}\gcd(g,2^k-1),
\]
with \(\gcd(g,0)=g\).

More precisely, if \(x=[\Theta(\mathbf c)]\) and
\[
h=|\{k\in\mathbb Z/m\mathbb Z:x^{2^k}=x\}|,
\]
then
\[
|\operatorname{Aut}E(\mathbf c)|=gh.
\]
Thus all nonzero weighted directed \(m\)-cycles collapse to one isomorphism class exactly when \(\gcd(2^m-1,q-1)=1\). For example, over \(\mathbb F_4\) in dimension \(2\), \(g=3\) and there are exactly two classes, so the complex-field normalization to unit weights has a genuine finite-field obstruction.

## Assumptions and scope
The field is exactly \(\mathbb F_q\), the support digraph is one directed cycle of length \(m\ge2\), and every cycle coefficient is nonzero. Isomorphisms are arbitrary algebra isomorphisms; they are not assumed in advance to preserve the displayed natural basis. The statement does not classify permutation evolution algebras with several cycle components or with zero structure constants.

These algebras satisfy \(E^2=E\), so they belong to the perfect/idempotent part of evolution-algebra theory. The invariant is a finite-field form obstruction: over an algebraically closed field the required \((2^m-1)\)-st roots exist and the obstruction disappears.

## Proof
Write an isomorphism \(\varphi:E(\mathbf c)\to E(\mathbf d)\) in the target natural basis as
\[
\varphi(e_i)=\sum_j a_{ji}f_j.
\]
For \(i\ne r\), the identity \(e_i e_r=0\) gives
\[
0=\varphi(e_i)\varphi(e_r)
 =\sum_j a_{ji}a_{jr}d_j f_{j+1}.
\]
Because every \(d_j\ne0\) and the \(f_{j+1}\) are distinct basis vectors, each row of \((a_{ji})\) contains at most one nonzero entry. Invertibility forces exactly one nonzero entry in every row and column. Hence every isomorphism is monomial:
\[
\varphi(e_i)=\lambda_i f_{\sigma(i)},\qquad \lambda_i\ne0.
\]
Comparing \(\varphi(e_i^2)\) with \(\varphi(e_i)^2\) gives both
\[
\sigma(i+1)=\sigma(i)+1\pmod m
\]
and
\[
c_i\lambda_{i+1}=\lambda_i^2d_{i+k},
\]
where \(\sigma(i)=i+k\). Thus the permutation part of an isomorphism is necessarily a rotation.

Iterating the scalar recurrence around the cycle yields
\[
\lambda_0^{2^m-1}
 =\frac{\Theta(\mathbf c)}{\Theta(\operatorname{rot}_k\mathbf d)}.
\]
Therefore the recurrence closes exactly when this ratio is an \(N\)-th power in \(\mathbb F_q^\times\). A one-step rotation satisfies
\[
\frac{\Theta(\mathbf d)^2}{\Theta(\operatorname{rot}_1\mathbf d)}=d_0^N,
\]
so in the quotient \(G=\mathbb F_q^\times/(\mathbb F_q^\times)^N\),
\[
[\Theta(\operatorname{rot}_k\mathbf d)]=[\Theta(\mathbf d)]^{2^k}.
\]
This proves the isomorphism criterion.

Since \(\mathbb F_q^\times\) is cyclic of order \(q-1\), \(G\) is cyclic of order \(g=\gcd(N,q-1)\). Because \(g\) is odd, doubling is an automorphism of \(G\), and because \(g\mid 2^m-1\), its \(m\)-th power is the identity. Every element of \(G\) occurs as a \(\Theta\)-class: varying only \(c_0\) gives the exponent \(2^{m-1}\), which is invertible modulo \(g\). Hence isomorphism classes are precisely the orbits of this cyclic action.

Burnside's lemma now gives the class count. The fixed points of the \(k\)-th power of doubling satisfy \(x^{2^k-1}=1\) in a cyclic group of order \(g\), so there are exactly \(\gcd(g,2^k-1)\) such points. Averaging over \(0\le k<m\) gives the displayed formula. Finally, for every stabilizing rotation the scalar closure equation has exactly \(g\) solutions in \(\mathbb F_q^\times\), the kernel size of the \(N\)-th power map, which gives \(|\operatorname{Aut}E(\mathbf c)|=gh\).

## Verification
The accompanying `verify.py` independently enumerates every invertible linear map for four small cases: \((q,m)=(3,2),(5,2),(4,2),(3,3)\). The \(q=4\) computation implements \(\mathbb F_4\) directly rather than treating it as a prime field. For every coefficient tuple and every pair of algebras in these cases, brute-force algebra-isomorphism testing agrees with the \(\Theta\)-orbit criterion; exact automorphism counts also agree with \(gh\). The same program directly compares Burnside's formula with orbit enumeration for seventeen field orders and every \(2\le m\le8\).

The finite computations are consistency checks only. The general result follows from the monomiality argument, the cycle-closing scalar recurrence, cyclicity of \(\mathbb F_q^\times\), and Burnside's lemma.

## Relationship to prior work
Khudoyberdiyev, Omirov and Qaralleh introduced the single-cycle normal form in their study of evolution algebras of permutations. Their full text treats the permutation family over characteristic zero and, in the relevant section, explicitly considers complex evolution algebras; Theorem 3.5 normalizes every nonzero weighted cycle to the unit-weight cycle by a scaling that uses the needed root extraction. The present finite-field result identifies exactly when that normalization descends to \(\mathbb F_q\), classifies all failures of descent, and counts the resulting forms in every dimension.

Narkuziyev's later work decomposes two-permutation evolution algebras into cycle components and studies absolute nilpotent and idempotent elements. Elduque and Labra place automorphisms of perfect evolution algebras in a graph-controlled exact sequence, which is consistent with the rotation-plus-diagonal structure used here but does not state this cross-algebra finite-field invariant or its class count. Wei and Zou give a general orbit framework for isomorphism classes of idempotent evolution algebras over finite fields and announce a general counting formula, with explicit total formulas in dimensions \(2,3,4\); the material inspected does not state the support-conditioned all-\(m\) cyclic formula above.

## Limitations
Only a single directed cycle with all weights nonzero is classified. Multiple-cycle permutation algebras can have additional component permutations and interactions among equal-length components, and are not covered here. The 2023 general finite-field classification was available only at abstract level during this comparison, so a residual risk remains that the displayed cyclic specialization is derivable or stated inside that broader framework; no such specialization was found in the inspected material or targeted record searches.

## References
1. A. Kh. Khudoyberdiyev, B. A. Omirov, I. Qaralleh, *Few remarks on evolution algebras*, arXiv:1307.0993 (first public 2013-07-03); Journal of Algebra and Its Applications 14 (2015), 1550053, doi:10.1142/S021949881550053X.
2. B. A. Narkuziyev, *On absolute nilpotent and idempotent elements of an evolution algebra corresponding to permutations*, arXiv:1803.11415.
3. B. A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, Journal of Algebra and Its Applications 21 (2022), 2250112, doi:10.1142/S0219498822501122.
4. A. Elduque, A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191; Linear and Multilinear Algebra 69 (2021), 331-342.
5. Y. Wei, Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, Linear Algebra and its Applications 675 (2023), 142-178, doi:10.1016/j.laa.2023.06.006.
