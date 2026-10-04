# The one-variable cardinality syllogistic has exactly five finite spectra
## Finding

Let
\[
\mathsf S^\dagger(\mathrm{card})[p]
\]
be the fragment of the finite-model syllogistic of Jiang in which there is exactly one raw variable \(p\), so the only nouns are
\[
p,\qquad \bar p.
\]

For any theory \(\Gamma\) in this one-variable fragment, its finite spectrum is exactly one of the following five sets:
\[
\varnothing,
\qquad
T_1=\mathbb N_{>0},
\qquad
T_2=\{n\ge2\},
\qquad
T_3=\{n\ge3\},
\qquad
E_2=\{n\ge2:n\text{ is even}\}.
\]

All five spectra occur. For example:
\[
\operatorname{Spec}(\varnothing)=T_1,
\]
\[
\operatorname{Spec}\bigl(\{\exists(p,p),\exists(\bar p,\bar p)\}\bigr)=T_2,
\]
\[
\operatorname{Spec}\bigl(\{\exists(p,p),\exists(\bar p,\bar p),\exists^>(p,\bar p)\}\bigr)=T_3,
\]
\[
\operatorname{Spec}\bigl(\{\exists^\ge(p,\bar p),\exists^\ge(\bar p,p)\}\bigr)=E_2,
\]
and
\[
\operatorname{Spec}\bigl(\{\exists^>(p,p)\}\bigr)=\varnothing.
\]

Thus the one-variable fragment has an exact spectrum ceiling: it cannot define \(T_k\) for any \(k\ge4\), nor \(E_k\) for any even threshold \(k\ge4\).

This gives the first finite-variable slice of Jiang's full classification, where unrestricted theories can realize every tail \(T_k\) and every even tail \(E_k\).

## Assumptions and scope

Models are finite and nonempty, as in Jiang's paper. A model consists of a finite universe \(M\) and an interpretation of \(p\) as a subset of \(M\); \(\bar p\) is interpreted as the complement.

The allowed sentence forms are exactly:
\[
\forall(x,y),\quad
\exists(x,y),\quad
\exists^\ge(x,y),\quad
\exists^>(x,y),
\]
where \(x,y\in\{p,\bar p\}\).

A theory is an arbitrary set of such sentences. Since there are only finitely many syntactic sentence forms over one raw variable, every one-variable theory is equivalent to a finite subtheory.

The result classifies spectra of theories in the original language, not the later sentence-level Boolean extension.

## Proof

Fix an \(n\)-element model and write
\[
k=|p|,
\qquad
|\bar p|=n-k.
\]

Every one-variable sentence is either a tautology, a contradiction, or one of eight nontrivial conditions on \(k\):

\[
k=0,
\qquad
k=n,
\qquad
k>0,
\qquad
k<n,
\]
\[
k\ge n-k,
\qquad
k\le n-k,
\qquad
k>n-k,
\qquad
k<n-k.
\]

Indeed:

- \(\forall(p,\bar p)\) says \(p=\varnothing\), hence \(k=0\);
- \(\forall(\bar p,p)\) says \(\bar p=\varnothing\), hence \(k=n\);
- \(\exists(p,p)\) says \(k>0\);
- \(\exists(\bar p,\bar p)\) says \(k<n\);
- the four cardinality-comparison sentences give the last four inequalities;
- the remaining same-noun universal and weak-cardinality comparisons are tautological;
- the remaining cross-noun existential sentences and same-noun strict comparisons are contradictory.

Therefore every consistent one-variable theory is equivalent to requiring
\[
L(n)\le k\le U(n),
\]
where the strongest lower bound \(L(n)\) is one of
\[
0,\quad
1,\quad
\left\lceil\frac n2\right\rceil,\quad
\left\lfloor\frac n2\right\rfloor+1,\quad
n,
\]
and the strongest upper bound \(U(n)\) is one of
\[
n,\quad
n-1,\quad
\left\lfloor\frac n2\right\rfloor,\quad
\left\lceil\frac n2\right\rceil-1,\quad
0.
\]

A model of size \(n\) exists exactly when
\[
L(n)\le U(n).
\]

The full feasibility table is:
\[
\begin{array}{c|ccccc}
L\backslash U&
n&
n-1&
\lfloor n/2\rfloor&
\lceil n/2\rceil-1&
0\\
\hline
0&T_1&T_1&T_1&T_1&T_1\\
1&T_1&T_2&T_2&T_3&\varnothing\\
\lceil n/2\rceil&T_1&T_2&E_2&\varnothing&\varnothing\\
\lfloor n/2\rfloor+1&T_1&T_3&\varnothing&\varnothing&\varnothing\\
n&T_1&\varnothing&\varnothing&\varnothing&\varnothing
\end{array}
\]
where each entry records the set of positive integers \(n\) for which the corresponding inequality is feasible.

For example,
\[
1\le \left\lceil\frac n2\right\rceil-1
\]
holds exactly when \(n\ge3\), producing \(T_3\), while
\[
\left\lceil\frac n2\right\rceil
\le
\left\lfloor\frac n2\right\rfloor
\]
holds exactly when \(n\) is even, producing \(E_2\).

No other spectrum can occur.

The displayed theories above realize every one of the five possibilities.

## Verification

The symbolic proof reduces the entire one-variable fragment to the \(5\times5\) lower/upper-bound table.

The bundled checker independently enumerates all subsets of the eight nontrivial one-variable semantic conditions, computes their spectra on universe sizes through \(64\), and verifies that exactly the five predicted patterns occur. It also checks the \(25\) strongest-bound pairs directly and verifies the concrete witness theories for all five spectra.

The finite replay is corroborative only. The proof of the classification is the exact reduction to the strongest lower and upper bounds and the closed-form comparison of those bounds.

## Relationship to prior work

Jiang proves that, with unrestricted raw variables, the finite spectra of \(\mathsf S^\dagger(\mathrm{card})\) are exactly
\[
\varnothing,\quad T_k,\quad E_k
\]
for arbitrary positive thresholds \(k\). The paper realizes large thresholds using chains of strict cardinality comparisons among many nouns and explains that the language can express lower bounds and parity.

The paper does not classify what happens when the raw-variable vocabulary is fixed to one variable. Its characteristic-theory construction deliberately introduces many raw variables so that many subsets of a finite universe can be named, and its general tail construction likewise uses a growing list of nouns.

The one-variable theorem therefore isolates a genuine vocabulary-size boundary inside the newly classified spectrum landscape: unrestricted lower thresholds disappear beyond \(3\), while the parity phenomenon already survives with one raw variable.

The earlier work of Moss and Moss--Topal develops the underlying syllogistic with cardinality comparisons and its proof theory, but the checked literature did not locate a finite-spectrum classification for the one-variable fragment.

## Limitations

The theorem is specific to one raw variable. It does not determine the exact spectrum hierarchy for two, three, or more raw variables.

The result classifies semantic spectra, not the number or syntactic complexity of theories producing each spectrum.

The Boolean sentence-level extension studied by Jiang can form unions of spectra and is not covered by this five-spectrum statement.

## References

[1] Ruiting Jiang, “Finite Spectra of Syllogistic Logic with Cardinality Comparisons,” arXiv:2609.24902, first posted 21 September 2026.

[2] Lawrence S. Moss, “Syllogistic Logic with Cardinality Comparisons,” in *J. Michael Dunn on Information Based Logics*, Springer, 2016, 391–415.

[3] Lawrence S. Moss and Selçuk Topal, “Syllogistic Logic with Cardinality Comparisons, On Infinite Sets,” *Review of Symbolic Logic* 13(1) (2020), 1–22. DOI:10.1017/S1755020318000126.
