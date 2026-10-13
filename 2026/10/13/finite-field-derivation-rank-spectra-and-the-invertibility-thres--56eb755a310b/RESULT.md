# Finite-field derivation-rank spectra and the invertibility threshold for a four-dimensional filiform Lie algebra

## Finding
Let \(q\) be any prime power and let \(L\) be the four-dimensional Lie algebra over \(\mathbb F_q\) with ordered basis \(e_1,e_2,e_3,e_4\) and only nonzero defining brackets
\[
[e_1,e_2]=e_3,\qquad [e_1,e_3]=e_4,
\]
together with their alternating counterparts. For an \(\mathbb F_q\)-linear derivation \(D\), its **rank** means its ordinary rank as a linear endomorphism of \(L\). Define
\[
P_q(z)=\sum_{D\in\operatorname{Der}_{\mathbb F_q}(L)}z^{\operatorname{rank}(D)}.
\]

For odd \(q\), the complete rank polynomial is
\[
\boxed{\begin{aligned}
P_q(z)={}&1+(q^3+q^2-q-1)z+(q-1)(2q^3-q)z^2\\
&+\bigl((q-1)^2q^3+4(q-1)q^5\bigr)z^3\\
&+(q-1)(q-3)q^5z^4.
\end{aligned}}
\]
For even \(q\), it is
\[
\boxed{\begin{aligned}
P_q(z)={}&1+(q^3+q^2-q-1)z\\
&+\bigl((q-1)(2q^3-q)+(q-1)q^4\bigr)z^2\\
&+\bigl((q-1)^2q^3+2(q-1)q^5+(q-1)^2q^4\bigr)z^3\\
&+(q-1)(q-2)q^5z^4.
\end{aligned}}
\]
In both cases, \(P_q(1)=q^7\), and every nonzero displayed coefficient counts exactly the derivations of that rank. Consequently, **a nonsingular derivation exists if and only if \(q\ge4\)**. In particular, the characteristic-two extension field \(\mathbb F_4\) admits invertible derivations, but \(\mathbb F_2\) and \(\mathbb F_3\) do not.

## Assumptions and scope
The Lie algebra is the standard four-dimensional model filiform Lie algebra, nilpotent of class three. The base field is any finite field, including nonprime extension fields and characteristics two and three. The map \(D\) ranges over every ordinary derivation satisfying \(D([u,v])=[D(u),v]+[u,D(v)]\) for all \(u,v\in L\); no automorphism, innerness, or semisimplicity restriction is imposed. The term *nonsingular* means invertible as an \(\mathbb F_q\)-linear endomorphism. The assertion does not generalize to arbitrary filiform deformations without a new calculation.

## Proof
**All derivations.** Write \(D(e_1)=a e_1+a_2e_2+a_3e_3+a_4e_4\) and \(D(e_2)=b_1e_1+b e_2+b_3e_3+b_4e_4\). Applying the derivation identity to \([e_2,e_3]=0\) forces \(b_1=0\). Applying it to the two nonzero brackets gives
\[
D(e_3)=(a+b)e_3+b_3e_4,\qquad
D(e_4)=(2a+b)e_4.
\]
Conversely these equations satisfy the derivation identity on every pair of basis vectors, including in characteristic two. Thus every derivation, uniquely, is represented by
\[
\boxed{D=\begin{pmatrix}
a&0&0&0\\
a_2&b&0&0\\
a_3&b_3&a+b&0\\
a_4&b_4&b_3&2a+b
\end{pmatrix}},
\]
with seven unrestricted parameters, yielding exactly \(q^7\) derivations.

**The common zero diagonal.** When \(a=b=0\), the rank is that of
\[
\begin{pmatrix}a_2&0&0\\a_3&b_3&0\\a_4&b_4&b_3\end{pmatrix}.
\]
If \(b_3\ne0\) and \(a_2\ne0\), its rank is three; this gives \((q-1)^2q^3\) choices. If \(b_3\ne0\) and \(a_2=0\), its rank is two, giving \((q-1)q^3\) choices. If \(b_3=0\), its rank is two precisely when \(b_4\ne0\) and \((a_2,a_3)\ne(0,0)\), giving \(q(q-1)(q^2-1)\) choices. The unique zero matrix has rank zero; all remaining \(q^3+q^2-q-1\) matrices have rank one. Hence on this diagonal-zero slice the rank-two count is \((q-1)(2q^3-q)\) and the rank-three count is \((q-1)^2q^3\).

**Odd characteristic.** For \((a,b)\ne(0,0)\), the four diagonal coefficients are \(a,b,a+b,2a+b\). Their zero loci are four distinct one-dimensional subspaces of \(\mathbb F_q^2\). Each of these contributes \(q-1\) nonzero pairs \((a,b)\), and on each line exactly one diagonal coefficient vanishes, so rank is three for every choice of the five off-diagonal parameters. Their total is \(4(q-1)q^5\). The remaining \((q-1)(q-3)\) pairs have all four diagonal coefficients nonzero, so each of their \(q^5\) associated matrices has rank four. Adding the zero-diagonal slice gives the odd formula. This includes \(q=3\), when the four lines exhaust all projective directions.

**Even characteristic.** Now the diagonal list is \(a,b,a+b,b\). There are two projective directions \(a=0\) and \(a=b\), each with \(q-1\) nonzero pairs; every associated matrix has rank three. The direction \(b=0\) with \(a\ne0\) is different: the rank is
\[
1+\operatorname{rank}\begin{pmatrix}b_3&a\\b_4&b_3\end{pmatrix}.
\]
It is two precisely when \(b_3^2+a b_4=0\). For each nonzero \(a\), this has exactly \(q\) solutions \((b_3,b_4)\); \(a_2,a_3,a_4\) remain arbitrary. Thus this direction contributes \((q-1)q^4\) rank-two matrices and \((q-1)^2q^4\) rank-three matrices. The remaining \((q-1)(q-2)\) pairs have no zero diagonal coefficients and contribute \((q-1)(q-2)q^5\) rank-four matrices. The even formula follows.

Both rank-four multiplicities are strictly positive exactly for the prime powers \(q\ge4\), as claimed.

## Verification
The accompanying standalone program `artifacts/verify.py` implements exact arithmetic over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). For each field it independently constructs the full linear Leibniz constraint matrix on all sixteen entries of a general endomorphism and confirms constraint rank nine. It then enumerates every one of the \(q^7\) seven-parameter derivations, calculates each matrix rank by finite-field Gaussian elimination, and compares the complete distribution with both formulas. Representative parameter matrices also satisfy every basis-pair Leibniz identity. The observed rank counts, ordered from rank zero to rank four, are
\[
\begin{array}{c|rrrrr}
q&0&1&2&3&4\\\hline
2&1&9&30&88&0\\
3&1&32&102&2052&0\\
4&1&75&1140&9024&6144\\
5&1&144&980&52000&25000
\end{array}.
\]
Run `python3 artifacts/verify.py` with Python 3; it prints `VERIFY_OK_FILIFORM_DERIVATIONS` on success. The proof above, rather than these finite computations, establishes the arbitrary-prime-power theorem.

## Relationship to prior work
Burde's *Lie Algebra Prederivations and Strongly Nilpotent Lie Algebras* (2004) places the existence of nonsingular derivations and prederivations at the center of the structural study of filiform Lie algebras. Its stated theorems classify obstructions in characteristic zero and higher dimensions; they do not give this exact finite-field rank distribution or the small-field threshold.

Casas, Ladra, Omirov and Karimjanov's *Classification of Solvable Leibniz Algebras with Naturally Graded Filiform Nilradical* (2012) uses derivations to construct solvable extensions over the complex field, and provides explicit matrix forms for related non-Lie nilradicals. Its classification is not a count of the operator ranks of all derivations of the four-dimensional Lie model over finite fields.

The published result *Adjoint-rank spectra of two maximal-class filiform Lie algebras* describes ranks of inner adjoint maps \(\operatorname{ad}_x\), not ranks of the entire derivation algebra, and its declared domain has dimension at least six. The published result *Almost-abelian Lie algebras have rank-only commutativity spectra* likewise concerns adjoint maps of a different family. These statements do not imply the present result by merely specializing a parameter. Existing descriptions of model-filiform automorphisms similarly do not count the ranks of all derivations.

## Limitations
An equivalent enumeration might exist in historical literature under an alternate name, so bibliographic priority is not certified. The theorem concerns one natural four-dimensional filiform Lie algebra, not all nilpotent Lie algebras. Finite-field experiments confirm the stated samples but do not independently prove the general formulas. No independent mathematical audit has been performed.

## References
1. D. Burde, *Lie Algebra Prederivations and Strongly Nilpotent Lie Algebras*, arXiv:math/0409276v1, first public 16 September 2004, particularly Sections 1–3.
2. J. M. Casas, M. Ladra, B. A. Omirov and I. A. Karimjanov, *Classification of Solvable Leibniz Algebras with Naturally Graded Filiform Nilradical*, arXiv:1203.4772v1, first public 21 March 2012, particularly Sections 2–4.
3. *Adjoint-rank spectra of two maximal-class filiform Lie algebras*, public mathematical result on the standard model and a second maximal-class family, consulted for statement and proof comparison.
4. *Almost-abelian Lie algebras have rank-only commutativity spectra*, public mathematical result on centralizer ranks in a different Lie family.
