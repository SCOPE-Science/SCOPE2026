# Exact time-support spectrum at rank-weighted Fourier size three on the tetrahedral group

## Finding
For \(G=A_4\), define \(\widehat f(\pi)=12^{-1}\sum_{g\in G} f(g)\pi(g)^*\) and the rank-weighted Fourier support \(\sigma(f)=\sum_{\pi\in\widehat G}(\dim\pi)\operatorname{rank}\widehat f(\pi)\). The following is an exact attainability theorem:

\[
\{|\operatorname{supp}f|:f\not\equiv0,\ \sigma(f)=3\}=\{4,6,8,9,10,11,12\}.
\]

In particular there are genuine support gaps at \(5\) and \(7\), beyond the usual bound \(|\operatorname{supp}f|\sigma(f)\ge 12\).

## Assumptions and scope
The field of coefficients is \(\mathbb C\); support means the number of nonzero point values. The four inequivalent complex irreducibles of \(A_4\) have dimensions \(1,1,1,3\). A real unitary model for the three-dimensional irreducible is the twelve matrices \(D_sP^j\), where \(j\in\{0,1,2\}\), \(P\) cyclically permutes the three coordinate axes, and \(D_s=\operatorname{diag}(s_1,s_2,s_3)\) with \(s_i\in\{-1,1\}\) and \(s_1s_2s_3=1\). The four diagonal sign matrices form a normal Klein four subgroup; the cyclic permutation acts transitively on its three nonidentity elements. These matrices realize \(A_4\), and the representation is irreducible: the commutant of the sign subgroup consists of diagonal matrices, and only scalars among these commute with \(P\).

## Proof
**Fourier-block dichotomy.** Since the irreducible dimensions are \(1,1,1,3\), the condition \(\sigma(f)=3\) allows exactly two Fourier configurations: all three one-dimensional blocks have rank one while the three-dimensional block vanishes; or the three-dimensional block has rank one and every one-dimensional block vanishes. In the former case \(f\) factors through \(A_4/V_4\cong\mathbb Z/3\mathbb Z\), and is constant on cosets of cardinality four. Its nonzero support is therefore one of \(4,8,12\).

**Matrix-coefficient form.** In the latter case, Fourier inversion and rank one imply that, up to a nonzero scalar, \(f(D_sP^j)=u^*D_sP^jv\) for nonzero vectors \(u,v\in\mathbb C^3\). Conversely Schur orthogonality gives \(\widehat f(\rho)=vu^*/3\) and zero one-dimensional blocks, so every such coefficient has \(\sigma(f)=3\).

**Parity-or-large-support obstruction.** For fixed \(j\), put \(a_i=\overline{u_i}(P^jv)_i\). The four values of \(f\) on the coset \(V_4P^j\) are
\[
a_1+a_2+a_3,\quad a_1-a_2-a_3,\quad -a_1+a_2-a_3,\quad -a_1-a_2+a_3.\]
If all coordinates of both \(u\) and \(v\) are nonzero, then all three \(a_i\) are nonzero in every coset. Two distinct listed values cannot both vanish: solving their two linear equations forces one of the three \(a_i\) to be zero. Thus each of the three cosets contributes at least three nonzero values, giving \(|\operatorname{supp}f|\ge9\).

If some coordinate of \(u\) or \(v\) vanishes, every coset has at least one zero among the three \(a_i\). Its four values then occur in opposite pairs, so the number of nonzero entries in that coset is \(0,2\), or \(4\), always even. Hence the total support cardinality is even. The standard rank-weighted uncertainty inequality yields \(|\operatorname{supp}f|\ge12/3=4\). Consequently only \(4,6,8,9,10,11,12\) can occur in either Fourier configuration.

**Attainability.** All seven sizes occur already as three-dimensional rank-one coefficients. In the same signed-permutation realization, choose respectively \((u,v)\) as
\[
\begin{array}{c|c|c}
|\operatorname{supp}f| &u&v\\\hline
4 &(1,0,0)&(1,0,0)\\
6 &(1,1,1)&(1,1,0)\\
8 &(1,1,0)&(1,0,0)\\
9 &(1,1,1)&(2,1,1)\\
10 &(2,2,1)&(2,2,1)\\
11 &(1,3,7)&(1,2,-1)\\
12 &(1,1,1)&(1,1,1)
\end{array}
\]
Direct evaluation of the twelve integer matrix coefficients yields exactly the displayed support sizes; the attached checker verifies every example and the Fourier-block identities. This finishes necessity and sufficiency.

## Verification
Run `python3 check_tetrahedral_support.py` using the ordinary Python standard library. The checker verifies the twelve signed-permutation matrices form a group; the full exact integer Schur orthogonality identities; rank-one Fourier-block identities and zero one-dimensional components; and all seven explicit witness cardinalities. Its additional finite integer-grid test is corroboration only; the exclusion of cardinalities \(5\) and \(7\) follows analytically from the parity-or-large-support argument, not enumeration.

## Relationship to prior work
Alagic and Russell's 2006 preprint, *Uncertainty Principles for Compact Groups* (arXiv:math/0608702), Theorem 2, establishes the general rank-weighted multiplicative uncertainty inequality. It implies the lower endpoint \(4\) here but does not determine the missing support cardinalities \(5\) and \(7\) for \(A_4\). General finite-group matrix-coefficient orthogonality is used, while the four-sign coset obstruction and complete attainability list are the specialization established here. No stronger primary result determining this exact support spectrum was identified in the sources inspected.

## Limitations
The classification concerns only \(\sigma(f)=3\), not all Fourier sizes on \(A_4\) or arbitrary finite groups. No assertion about functions restricted to be nonnegative or real is made. Source coverage may be incomplete; independent examination of novelty and the proof has not been performed.

## References
1. G. Alagic and A. Russell, *Uncertainty Principles for Compact Groups*, arXiv:math/0608702 (first publicly submitted 2006-08-28); Theorem 2 and Sections 2–3. https://arxiv.org/abs/math/0608702
2. Standard finite-group Schur orthogonality and Fourier inversion, as used and stated in the preceding reference.
