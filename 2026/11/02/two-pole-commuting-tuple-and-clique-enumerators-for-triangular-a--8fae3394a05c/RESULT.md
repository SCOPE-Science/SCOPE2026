# Two-pole commuting-tuple and clique enumerators for triangular algebras over finite chain rings

## Finding

Let \(R\) be a nonzero finite commutative chain ring, \(\mathfrak m=(\pi)\) its maximal ideal, \(\mathfrak m^\ell=0\ne\mathfrak m^{\ell-1}\), and \(q=|R/\mathfrak m|\). Here \(\ell\ge1\) and \(q\) is a prime power. Let \(T=\operatorname{Tr}_2(R)\) denote the *algebra* of **all** upper triangular two-by-two matrices, with no invertibility restriction. For every integer \(k\ge0\), count ordered tuples with unrestricted repetitions:
\[
C_k(R)=|\{(A_1,\dots,A_k)\in T^k:A_iA_j=A_jA_i\text{ for all }i,j\}|.
\]
Define the integer \(S_\ell(q)=1+q+\cdots+q^\ell\). Then the entire simultaneous-commutation sequence is
\[
\boxed{C_k(R)=S_\ell(q)q^{2\ell k}-(S_\ell(q)-1)q^{(2\ell-1)k}}\quad(k\ge0).
\]
Equivalently its ordinary generating function has precisely two possible poles:
\[
\boxed{\sum_{k\ge0}C_k(R)z^k=
\frac{S_\ell(q)}{1-q^{2\ell}z}-
\frac{S_\ell(q)-1}{1-q^{2\ell-1}z}}.
\]

Let \(f_r(T)\) be the number of \(r\)-element *sets of distinct* matrices that are pairwise commuting, with \(f_0(T)=1\). Their complete clique polynomial (including scalar matrices as vertices) is
\[
\boxed{\sum_{r\ge0}f_r(T)z^r=
S_\ell(q)(1+z)^{q^{2\ell}}-
(S_\ell(q)-1)(1+z)^{q^{2\ell-1}}}.
\]
In particular, for all \(r\ge0\),
\[
\boxed{f_r(T)=S_\ell(q)\binom{q^{2\ell}}r-
(S_\ell(q)-1)\binom{q^{2\ell-1}}r}.
\]
As a consequence the maximum size of a pairwise commuting set is \(q^{2\ell}\), and there are \(S_\ell(q)\) such maximum sets. This extremal count is included as an implication and is *not* presented as a new theorem in the cyclic-ring special case.

For the usual simple commuting graph on noncentral matrices, the center comprises the \(q^\ell\) scalar matrices and is adjacent to everything in the full commuting relation. Its clique polynomial is therefore
\[
\boxed{\sum_{r\ge0}f_r(T\setminus Z(T))z^r=
S_\ell(q)(1+z)^{q^{2\ell}-q^\ell}-
(S_\ell(q)-1)(1+z)^{q^{2\ell-1}-q^\ell}}.
\]
Both formulas depend only on \((q,\ell)\), even though chain rings with those parameters can have different characteristics and additive groups. For every finite commutative principal ideal ring, the ordered-tuple counts factor as the product of these formulas over its local chain-ring factors.

## Assumptions and scope

A finite commutative chain ring is a finite unital local ring whose ideals are \(R\supset\pi R\supset\dots\supset\pi^\ell R=0\), with successive quotients all of size \(q\). Thus \(|R|=q^\ell\). The zero ring is excluded. The theorem is for arbitrary finite residue fields and arbitrary characteristic, including characteristic two and mixed-characteristic chain rings. The full graph includes all \(|T|=q^{3\ell}\) algebra elements. For the noncentral graph all scalar matrices are removed; the empty clique is counted once. There is no implied restriction that the tuple elements commute with only their neighbors: every pair must commute. The case \(k=0\) is the one empty tuple and is included in the displayed formula.

## Proof

**1. Reduction to determinant-zero matrices.** Every element of \(T\) is uniquely
\[
A(c,x,y)=\begin{pmatrix}c+x&y\\0&c\end{pmatrix},\qquad c,x,y\in R.
\]
Direct multiplication gives
\[
[A(c,x,y),A(d,u,v)]=
\begin{pmatrix}0&xv-uy\\0&0\end{pmatrix}.
\]
Therefore a tuple commutes pairwise if and only if the column vectors \((x_i,y_i)\) form a \(2\times k\) matrix whose every \(2\times2\) minor vanishes in \(R\). The scalars \(c_i\) are independent and contribute \(q^{\ell k}\). Let \(D_{\ell,k}\) denote the count of the determinant-zero \(2\times k\) matrices. We must show
\[
D_{\ell,k}=S_\ell(q)q^{\ell k}-(S_\ell(q)-1)q^{(\ell-1)k}.
\]
For \(k=0\), both sides equal one. Fix \(k\ge1\) henceforth.

**2. Primitive matrix lemma.** In any finite chain ring \(R_m\) of length \(m\ge1\) and residue-field size \(q\), the number of \(2\times k\) matrices with at least one unit entry and all \(2\times2\) minors zero is
\[
P_{m,k}=(q+1)(q^k-1)q^{(k+1)(m-1)}.
\]
Indeed, choose a unit entry as pivot. Vanishing of all minors forces each entry to be the product of one row coefficient and one column coefficient after dividing by that unit, so the matrix is a primitive outer product \(ab\), where \(a\in R_m^2\) is a primitive column and \(b\in R_m^k\) a primitive row. There are \(q^{2m}-q^{2m-2}\) choices for \(a\) and \(q^{km}-q^{k(m-1)}\) choices for \(b\). Every matrix has exactly \(q^m-q^{m-1}\) such presentations, by the unique simultaneous unit rescaling of the two factors. Dividing gives the formula. This argument uses only the chain of ideals, not a coefficient-field section.

**3. Valuation shells.** Write \(v(0)=\ell\) and \(v(a)=t\) when \(a\in\pi^tR\setminus\pi^{t+1}R\). For the \(2k\) matrix entries, let \(t\) be the minimum valuation. If \(t\ge h=\lceil\ell/2\rceil\), all pairwise determinants vanish automatically. There are exactly
\[
q^{2k\lfloor\ell/2\rfloor}
\]
such deep matrices, since all entries lie in \(\pi^hR\).

For each \(0\le t<h\), divide each entry by \(\pi^t\), represented in \(R/\pi^{\ell-t}R\). The reduced matrix is primitive. Its minors vanish in \(R\) precisely when its image in \(R/\pi^{\ell-2t}R\) has vanishing minors. This image remains primitive. Each of its \(2k\) entries has exactly \(q^t\) lifts to the longer quotient, so shell \(t\) contains precisely
\[
q^{2kt}P_{\ell-2t,k}
=(q+1)(q^k-1)q^{2kt+(k+1)(\ell-2t-1)}
\]
matrices. These shells and the deep matrices partition all determinant-zero matrices, with no double counting.

Define
\[
W_\ell(q)=(q+1)\sum_{t=0}^{\lceil\ell/2\rceil-1}q^{\ell-1-2t}.
\]
The exponents in this sum are nonnegative. Summing the shell formula and extracting \(q^{k(\ell-1)}\) yields
\[
D_{\ell,k}=q^{2k\lfloor\ell/2\rfloor}+
W_\ell(q)\bigl(q^{\ell k}-q^{(\ell-1)k}\bigr).
\]
If \(\ell\) is even, the geometric sum gives \(W_\ell(q)=S_\ell(q)-1\) and \(2\lfloor\ell/2\rfloor=\ell\). If \(\ell\) is odd, it gives \(W_\ell(q)=S_\ell(q)\) and \(2\lfloor\ell/2\rfloor=\ell-1\). In either case the same two-term identity follows:
\[
D_{\ell,k}=S_\ell(q)q^{\ell k}-(S_\ell(q)-1)q^{(\ell-1)k}.
\]
Multiplying by the \(q^{\ell k}\) unconstrained scalar coordinates proves the ordered-tuple formula, including the already checked \(k=0\) case. The ordinary generating function follows by summing two geometric series, as a formal identity.

**4. All distinct clique sizes.** For a finite simple graph, an ordered pairwise-compatible tuple has a unique set of \(r\) distinct values. A chosen size-\(r\) clique admits exactly \(r!\,\bigl\{\begin{smallmatrix}k\\r\end{smallmatrix}\bigr\}\) surjective ordered \(k\)-tuples, where braces denote Stirling numbers of the second kind. Equivalently,
\[
\sum_{k\ge0}C_k(R)\frac{t^k}{k!}
=\sum_{r\ge0}f_r(T)(e^t-1)^r.
\]
The two-term formula for \(C_k\) turns the left side into
\(S_\ell(q)e^{q^{2\ell}t}-(S_\ell(q)-1)e^{q^{2\ell-1}t}\).
Set \(z=e^t-1\), or invert the Stirling transform formally, to obtain the full clique polynomial and binomial-coefficient formula. Its degree is exactly \(q^{2\ell}\), with leading coefficient \(S_\ell(q)\); hence precisely that many maximum-sized cliques occur.

Every scalar matrix commutes with all elements of \(T\), and there are exactly \(q^\ell\) scalars. Removing this complete universal vertex set divides the full clique polynomial by \((1+z)^{q^\ell}\), proving the noncentral formula. Finally, if \(R\cong\prod_iR_i\), the triangular algebra and its coordinatewise commuting relation factor across the product, giving \(C_k(R)=\prod_i C_k(R_i)\).

## Verification

Run the included standalone script with `python verify.py` (Python standard library only). It independently constructs both integer residue rings and truncated-polynomial rings, performs actual ring multiplication and determinant checks, and enumerates all ordered commuting tuples for ten finite configurations. It additionally enumerates isotropic two-generator submodules in nine configurations, directly enumerates all two- and three-element commuting subsets in eight graph configurations, and checks 360 parameter triples in the closed identity. Successful output contains `TUPLE_CENSUS_OK 10`, `MAXIMAL_CLIQUES_OK 9`, `FORMULA_IDENTITY_OK 360`, and `CLIQUE_F_VECTOR_OK 8`.

For example, when \(q=2\) and \(\ell=2\), the formula gives \(C_3=25{,}600\), whereas over both \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[t]/(t^2)\), direct enumeration returns that value. In the same setting, there are \(672\) two-element commuting subsets, \(3{,}584\) three-element commuting subsets, and exactly \(7\) maximum-sized commuting subsets. These finite tests corroborate the general algebraic proof but are not substituted for it.

## Relationship to prior work

Cheraghpour, Ghosseiri, Jafari, and Seyfpour's 2024 study of commuting graphs of upper triangular rings proves the determinant criterion, finite-field component structure, the number of edges for some residue rings, and maximum clique sizes. Its finite-field clique decomposition yields the length-one boundary of our formulas. For prime-power residue rings its edge counts concern commuting pairs, not a closed enumeration of all ordered arities and all distinct clique sizes. The primary statements are available in the complete open-access text, including their theorems, examples, and concluding discussion.

Kaur, Sharma, and Singh study commuting tuples in the *invertible* upper triangular groups and unitriangular groups over odd finite fields, using branching rules and low-arity probabilities. Their objects and hypotheses do not give the unrestricted algebra counts over arbitrary chain rings.

An existing rank-two isotropic-submodule theorem already counts maximum determinant-zero subsets of \((\mathbb Z/p^a\mathbb Z)^2\). Its maximum-clique count is a prior result in an equivalent cyclic-ring setting, and our formula's top coefficient is explicitly **not** asserted as a novel standalone count. The claimed addition is the uniform *complete* clique-size distribution and unrestricted all-arity tuple formula for every finite commutative chain ring. A broader enumeration of determinantal congruences might imply the same identities; no publication-priority or independence claim is made.

## Limitations

The theorem applies to two-by-two upper triangular **algebras** over finite commutative chain rings; for noncommutative base rings, higher triangular size, or arbitrary finite local rings with nonprincipal radical, the determinant reduction and shell count need not work. The simple commuting graph is defined on noncentral elements, but its clique polynomial follows only by the stated universal-center factorization. The polynomial records clique counts, not graph isomorphism or clique homotopy type. The proof is complete for the stated domain, while independently established publication priority remains outside its scope. The relevant literature on general determinantal congruence point counts is a residual originality risk. All computational tests are finite and establish no theorem beyond their enumerated configurations.

## References

1. H. Cheraghpour, M. N. Ghosseiri, M. Jafari, and F. Seyfpour, “On Commuting graphs of triangular rings,” arXiv:2402.12619v1, first publicly posted 20 February 2024, https://arxiv.org/html/2402.12619v1. Primary MSC2020 16S50.
2. D. Kaur, U. B. Sharma, and A. Singh, “Branching rules and commuting probabilities for Triangular and Unitriangular matrices,” arXiv:2006.01493v1, first publicly posted 2 June 2020, https://arxiv.org/abs/2006.01493.
3. “Maximum pairwise lift-commuting subsets in \(C_{p^a}\times C_{p^a}\),” an earlier publicly available rank-two maximal-isotropic-subgroup classification. The overlap concerns the extremal count only, not the entire clique polynomial.
