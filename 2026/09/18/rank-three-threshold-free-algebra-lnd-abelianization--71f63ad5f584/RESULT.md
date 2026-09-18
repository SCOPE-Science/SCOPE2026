# A rank-three threshold for abelianization of free-algebra locally nilpotent derivations

## Result

Let \(k\) be a field and
\[
F_n=k\langle x_1,\ldots,x_n\rangle,\qquad
P_n=k[x_1,\ldots,x_n],
\]
with the natural abelianization map \(\pi:F_n\to P_n\). Every derivation of \(F_n\) preserves the commutator ideal, hence induces a derivation of \(P_n\); write
\[
\pi_*:\operatorname{Der}(F_n)\longrightarrow \operatorname{Der}(P_n)
\]
for this map.

Fix \(i\), put
\[
B_i=k\langle x_j:j\ne i\rangle,\qquad
\overline B_i=k[x_j:j\ne i],
\]
and let \(I_i=\ker(B_i\to\overline B_i)\), the commutator ideal of \(B_i\). For \(w\in B_i\), define
\[
D_w(x_i)=w,\qquad D_w(x_j)=0\quad(j\ne i).
\]
Then every \(D_w\) is locally nilpotent, the map \(w\mapsto D_w\) is injective and \(k\)-linear, and
\[
\pi_*(D_w)=\overline w\,\partial_{x_i}.
\]
Consequently the elementary triangular locally nilpotent derivations fit into an exact sequence
\[
0\longrightarrow I_i
\longrightarrow \{D_w:w\in B_i\}
\xrightarrow{\ \pi_*\ }
\overline B_i\,\partial_{x_i}
\longrightarrow0.
\]

Equivalently, for every \(f\in\overline B_i\) and every lift \(\widetilde f\in B_i\), the elementary locally nilpotent lifts of
\(f\partial_{x_i}\) are exactly
\[
\{D_{\widetilde f+c}:c\in I_i\}.
\]
Thus, as soon as \(n\ge3\), every elementary commutative locally nilpotent derivation \(f(x_1,\ldots,\widehat{x_i},\ldots,x_n)\partial_{x_i}\) has an infinite-dimensional affine family of noncommutative locally nilpotent lifts with the same abelianization.

If \(m=n-1\), the homogeneous degree-\(d\) part of the invisible kernel has dimension
\[
\dim_k (I_i)_d
=
m^d-\binom{m+d-1}{d},
\]
and hence
\[
H_{I_i}(t)
=
\frac{1}{1-mt}-\frac{1}{(1-t)^m}.
\]
For \(m\ge2\) this is infinite-dimensional and grows exponentially in degree.

In particular, over an algebraically closed field of characteristic zero,
\[
\boxed{
\ker(\pi_*)\cap \operatorname{LND}(F_n)=\{0\}
\quad\Longleftrightarrow\quad n\le2.
}
\]
The \(n=2\) direction is Corollary 28 of Baltazar--Lopes--Morales; the \(n=1\) case is immediate. For \(n\ge3\), an explicit nonzero element of the kernel is
\[
D(x_1)=[x_2,x_3],\qquad
D(x_j)=0\quad(j\ge2).
\]

This gives a sharp rank threshold: the rank-two detection of locally nilpotent derivations by abelianization disappears already in rank three.

## Proof

The assignment on the free generators uniquely defines a derivation \(D_w\). For a word \(u\), let \(\nu_i(u)\) be the number of occurrences of \(x_i\). Because \(w\) contains no \(x_i\), applying \(D_w\) to a word replaces one occurrence of \(x_i\) by \(w\). Hence every monomial appearing in \(D_w(u)\) has \(x_i\)-count \(\nu_i(u)-1\). It follows that
\[
D_w^{\,\nu_i(u)+1}(u)=0.
\]
For a polynomial, take the maximum \(x_i\)-count among its finitely many monomials. Thus \(D_w\) is locally nilpotent.

The map \(w\mapsto D_w\) is injective because \(D_w(x_i)=w\), and it is visibly \(k\)-linear. Passing to the commutative quotient gives
\[
\pi_*(D_w)(x_i)=\overline w,\qquad
\pi_*(D_w)(x_j)=0\quad(j\ne i),
\]
so \(\pi_*(D_w)=\overline w\,\partial_{x_i}\). Since \(B_i\to\overline B_i\) is surjective with kernel \(I_i\), the exact sequence and the affine-fiber description follow.

The standard word-length grading gives
\[
\dim_k(B_i)_d=m^d,\qquad
\dim_k(\overline B_i)_d=\binom{m+d-1}{d}.
\]
Abelianization is graded and surjective, so subtracting dimensions yields
\[
\dim_k(I_i)_d=m^d-\binom{m+d-1}{d},
\]
and summing over \(d\ge0\) gives the stated Hilbert series. When \(m=1\), \(B_i\) is already commutative and \(I_i=0\). When \(m\ge2\), for example the elements
\[
[x_2,x_3]x_2^r,\qquad r\ge0,
\]
are linearly independent elements of \(I_1\), so the kernel is nonzero and infinite-dimensional.

For the global threshold in characteristic zero, Baltazar--Lopes--Morales prove for \(F_2=k\langle x,y\rangle\) over their standing algebraically closed characteristic-zero field that
\[
\ker(\pi_*)\cap\operatorname{LND}(F_2)=\{0\}.
\]
The construction above supplies nonzero elements of this intersection for every \(n\ge3\), while \(F_1=k[x_1]\) has trivial abelianization kernel. This proves the equivalence.

## Isotropy and one-parameter subgroups

For \(q\in B_i\), define
\[
\tau_q(x_i)=x_i+q,\qquad
\tau_q(x_j)=x_j\quad(j\ne i).
\]
Then \(\tau_q^{-1}=\tau_{-q}\), and
\[
\tau_qD_w=D_w\tau_q
\]
because both \(q\) and \(w\) lie in the subalgebra fixed pointwise by \(D_w\) and by \(\tau_q\). Thus the isotropy group of every \(D_w\) contains an additive subgroup
\[
\{\tau_q:q\in B_i\}\cong (B_i,+).
\]
Its subgroup with \(q\in I_i\) acts trivially on abelianization. Over characteristic zero,
\[
\exp(tD_w)=\tau_{tw},
\]
so every nonzero invisible \(D_w\) produces a nontrivial one-parameter unipotent automorphism that is itself invisible after abelianization.

The mechanism behind the rank threshold is therefore simple but structural. In rank two, a nonzero commutator necessarily involves the active variable if only one other variable is fixed; Baltazar--Lopes--Morales exploit rank-two triangularization to obtain zero-detection. Starting in rank three, two frozen noncommuting variables are available, so a nonzero commutator can be used as the coefficient of a locally nilpotent elementary derivation without ever being differentiated.

## Relation to prior work and limitations

Baltazar, Lopes and Morales, arXiv:2609.19470v1, analyze abelianization for \(k\langle x,y\rangle\). Their Corollary 28 proves that no nonzero locally nilpotent derivation of the rank-two free algebra vanishes after abelianization. Their Proposition 29 also exhibits a derivation whose abelianization is locally nilpotent while the original derivation is not. The theorem above identifies a different phenomenon beginning in rank three: entire infinite-dimensional families of genuinely locally nilpotent derivations become invisible, and every elementary commutative locally nilpotent derivation acquires such a family of lifts.

The triangulability and kernel theory of locally nilpotent derivations of the rank-two free associative algebra were studied earlier by Crode--Shestakov and by Drensky--Makar-Limanov. Rank-three free associative automorphisms and coordinates were surveyed by Drensky--Yu. These are prior work and no novelty is claimed for triangular automorphisms, the commutator ideal itself, or the elementary fact that \(D_w\) is locally nilpotent when \(w\) uses only fixed variables.

The novelty claim is restricted to the sharp abelianization threshold, the exact elementary-LND fiber description, and the graded size formula for the invisible locally nilpotent kernel. Targeted searches using abelianization/commutativization, locally nilpotent derivations, rank three, commutator-ideal coefficients, and the explicit prototype \(D(x_1)=[x_2,x_3]\) did not locate an equivalent statement. Originality is therefore only to the best of our knowledge.

The full texts of the 2020 Crode--Shestakov article and the 2007 Drensky--Yu survey were not inspected here; their available abstracts and bibliographic descriptions respectively concern rank-two triangulability and rank-three automorphisms/coordinates. They remain the most plausible older sources in which an equivalent elementary observation could have appeared under different terminology. The recent source arXiv:2609.19470 is a first version and may also be revised.

## References

1. R. Baltazar, S. Lopes, O. Morales, *A Characterization of Local Nilpotence for Derivations of Ore Extensions*, arXiv:2609.19470v1, 2026. https://arxiv.org/abs/2609.19470
2. S. D. Crode, I. P. Shestakov, *Locally nilpotent derivations and automorphisms of free associative algebra with two generators*, Communications in Algebra 48 (2020), 3091--3098. https://doi.org/10.1080/00927872.2020.1729363
3. V. Drensky, L. Makar-Limanov, *Locally Nilpotent Derivations of Free Algebra of Rank Two*, SIGMA 15 (2019), 091. https://arxiv.org/abs/1909.13262
4. V. Drensky, J.-T. Yu, *Coordinates and automorphisms of polynomial and free associative algebras of rank three*, Frontiers of Mathematics in China 2 (2007), 13--46. https://doi.org/10.1007/s11464-007-0002-9
