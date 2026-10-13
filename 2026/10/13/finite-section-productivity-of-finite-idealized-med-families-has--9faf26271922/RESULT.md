# Finite-section productivity of finite idealized MED families has an exact fiber criterion
## Finding

Let \(F\) be a partial function from a countable set to \((\omega+1)\setminus\{0\}\) with infinite domain \(D\), let \(\mathcal J\) be a proper ideal on \(D\), and let \(\mathcal E=\{f_0,\ldots,f_{k-1}\}\subseteq\mathcal N_F\) be a finite \(\mathcal J\)-eventually-different family of size \(1\le k<\omega\). Put \(C_k=\{n\in D:F(n)=k\}\). Then \(\mathcal E\) is finite-section productive \(\mathcal J\)-MED if and only if \(C_k\in\mathcal J^+\). Consequently, a finite-section productive \(\mathcal J\)-MED family of size \(k\) exists if and only if both \(\{n\in D:F(n)\ge k\}\in\mathcal J^*\) and \(C_k\in\mathcal J^+\). In contrast, the recent finite Van Douwen classification requires the stronger condition \(C_k\in\mathcal J^*\). Hence the two finite notions are sharply separated: for \(\mathcal J=\mathrm{Fin}\) and \(F(2m)=k,\ F(2m+1)=k+1\), an FSP family of size \(k\) exists, but no Van Douwen family of size \(k\) exists.

The criterion is independent of the particular finite eventually-different family once its size is fixed: among existing \(\mathcal J\)-eventually-different \(k\)-families, finite-section productivity is controlled exactly by whether the fiber \(F^{-1}(\{k\})\) is \(\mathcal J\)-positive.

## Assumptions and scope

Let \(D=\operatorname{dom}(F)\) be infinite and countable, with
\[
F:D\to(\omega+1)\setminus\{0\},
\qquad
\mathcal N_F=\prod_{n\in D}F(n).
\]
Let \(\mathcal J\) be a proper ideal on \(D\), with dual filter \(\mathcal J^*\) and positive sets \(\mathcal J^+\). For \(f,g\in\mathcal N_F\), write
\[
\operatorname{Eq}_D(f,g)=\{n\in D:f(n)=g(n)\}.
\]
A family is \(\mathcal J\)-eventually different when every equality set between distinct members lies in \(\mathcal J\).

The finite-section productive notion and its ultrafilter characterization are those of He, Luo and Zhang. The theorem concerns finite families only. No assertion is made about infinite FSP families.

## Proof

Fix
\[
\mathcal E=\{f_0,\ldots,f_{k-1}\}
\]
with \(1\le k<\omega\), and define
\[
B=\bigcap_{i<j<k}\{n:f_i(n)\ne f_j(n)\}.
\]
Because every \(\operatorname{Eq}_D(f_i,f_j)\) lies in \(\mathcal J\) and there are only finitely many pairs,
\[
B\in\mathcal J^*.
\]
At each \(n\in B\), the \(k\) values \(f_0(n),\ldots,f_{k-1}(n)\) are distinct, so
\[
B\subseteq G_k:=\{n:F(n)\ge k\}.
\]

Suppose first that \(\mathcal E\) is FSP \(\mathcal J\)-MED. By Lemma 4.23 of He--Luo--Zhang, there is an ultrafilter \(\mathcal U\) on \(D\) with
\[
\mathcal J^*\subseteq\mathcal U
\]
such that \(\mathcal E\) is \(\mathcal U^*\)-MED. In particular \(B\in\mathcal U\).

Let
\[
C_k=\{n:F(n)=k\}.
\]
Assume toward a contradiction that \(C_k\notin\mathcal U\). Then
\[
A=B\cap(D\setminus C_k)\in\mathcal U.
\]
For every \(n\in A\), the \(k\) values \(f_i(n)\) are distinct and \(F(n)\ne k\). Since \(F(n)\ge k\) on \(B\), it follows that \(F(n)>k\). Choose
\[
h(n)\in F(n)\setminus\{f_i(n):i<k\}
\]
for \(n\in A\), and choose \(h(n)\) arbitrarily in \(F(n)\) elsewhere. Then for every \(i<k\),
\[
A\cap\operatorname{Eq}_D(h,f_i)=\varnothing.
\]
Because \(A\in\mathcal U\), no equality set \(\operatorname{Eq}_D(h,f_i)\) belongs to \(\mathcal U\), contradicting \(\mathcal U^*\)-maximality. Hence \(C_k\in\mathcal U\), and therefore
\[
C_k\in\mathcal J^+.
\]

Conversely, assume \(C_k\in\mathcal J^+\). The family
\[
\mathcal J^*\cup\{C_k\}
\]
has the finite-intersection property, so extend it to an ultrafilter \(\mathcal U\). Since \(B\in\mathcal J^*\), we have
\[
B\cap C_k\in\mathcal U.
\]
For every \(n\in B\cap C_k\), the \(k\) distinct values \(f_0(n),\ldots,f_{k-1}(n)\) exhaust the \(k\)-element set \(F(n)\). Thus for every \(h\in\mathcal N_F\),
\[
B\cap C_k\subseteq\bigcup_{i<k}\operatorname{Eq}_D(h,f_i).
\]
The finite union on the right belongs to \(\mathcal U\), so ultrafilter primeness gives some \(i<k\) with
\[
\operatorname{Eq}_D(h,f_i)\in\mathcal U.
\]
Also \(\mathcal E\) is \(\mathcal U^*\)-eventually different because \(\mathcal J\subseteq\mathcal U^*\). Therefore \(\mathcal E\) is \(\mathcal U^*\)-MED. Lemma 4.23 now yields that \(\mathcal E\) is FSP \(\mathcal J\)-MED.

It remains to extract the existence criterion. A \(\mathcal J\)-eventually-different family of size \(k\) exists exactly when
\[
G_k=\{n:F(n)\ge k\}\in\mathcal J^*.
\]
Necessity follows from \(B\subseteq G_k\). For sufficiency, when \(G_k\in\mathcal J^*\), define
\[
f_i(n)=
\begin{cases}
i,&n\in G_k,\\
0,&n\notin G_k,
\end{cases}
\qquad i<k.
\]
These functions belong to \(\mathcal N_F\), and any two agree only outside \(G_k\), a set in \(\mathcal J\). Combining this with the first equivalence gives the stated two-condition existence theorem.

Finally, take \(D=\omega\), \(\mathcal J=\mathrm{Fin}\), and
\[
F(2m)=k,\qquad F(2m+1)=k+1.
\]
Then \(G_k=\omega\in\mathrm{Fin}^*\), while \(C_k\) is the even integers: it is infinite, hence \(\mathrm{Fin}\)-positive, but not cofinite. The FSP criterion gives a finite FSP family of size \(k\), whereas Proposition 3.3 of He--Luo--Zhang rules out a finite Van Douwen family of size \(k\).

## Verification

The proof is symbolic and has no finite-search or numerical-completeness step. The critical checks are:

1. finite \(\mathcal J\)-eventual difference makes the simultaneous pairwise-distinct set \(B\) belong to \(\mathcal J^*\);
2. an FSP witness ultrafilter cannot concentrate where \(F(n)>k\), because there one can diagonalize pointwise against all \(k\) members;
3. if an ultrafilter concentrates on \(F(n)=k\), pairwise distinctness forces the \(k\) members to exhaust every coordinate and ultrafilter primeness selects one equality class for each \(h\);
4. existence of a \(k\)-member \(\mathcal J\)-eventually-different family is equivalent to \(\{n:F(n)\ge k\}\in\mathcal J^*\);
5. the alternating example satisfies the FSP conditions but fails the published Van Douwen condition.

The argument remains valid when some \(F(n)=\omega\): on the diagonalization set, \(F(n)>k\) still supplies a value outside the \(k\) displayed values.

## Relationship to prior work

He, Luo and Zhang characterize finite Van Douwen \(\mathcal J\)-MED families: a family of size \(k\) exists exactly when
\[
\{n:F(n)=k\}\in\mathcal J^*.
\]
They separately introduce finite-section productivity and prove that an FSP \(\mathcal J\)-MED family is exactly a \(\mathcal U^*\)-MED family for some ultrafilter \(\mathcal U\supseteq\mathcal J^*\). Their Stone-space theorem gives a general topological description of FSP and Van Douwen maximality.

The present result combines the ultrafilter characterization with a finite-cardinality diagonalization that is absent from the stated finite Van Douwen theorem. It identifies the exact finite FSP threshold and shows that the two notions differ by a sharp ideal-theoretic boundary: positivity of the exact \(k\)-fiber suffices for FSP, whereas co-largeness of that fiber is required for Van Douwen maximality.

Targeted searches for finite FSP families, finite-section productive eventually-different families, exact \(F(n)=k\) fiber criteria, and ultrafilter-maximal finite families did not locate this classification. Earlier work on productivity of MED families uses a different finite-product notion and is background rather than evidence for the exact idealized FSP criterion here.

## Limitations

The theorem is only for finite \(\mathcal J\)-eventually-different families. It does not classify infinite FSP families, Borel or analytic complexity, or the cardinal invariants governing infinite intersections in the Stone-space hierarchy.

The criterion assumes the same product-space convention \(F(n)\in(\omega+1)\setminus\{0\}\) as the source. It does not address alternative codomain conventions.

## References

1. Jialiang He, Jintao Luo, Hang Zhang, “Van Douwen Families, Productivity and Ultrafilter Maximality,” arXiv:2610.02350v1, first posted 1 October 2026. See Proposition 3.3, Lemma 4.23, and Theorem 5.2.
2. Lukas Schembecker, “Productivity of maximal eventually different families,” arXiv:2606.18137v1, first posted 16 June 2026.
