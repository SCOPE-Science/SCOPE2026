# Ultrafilter boundary for conjunction-preserving \(\omega\)-accumulation

## Finding

Let \(X\) be any topological space. For each \(A\subseteq X\), put
\[
D_{\omega}(A)=\{x\in X:\text{every open neighbourhood }U\ni x\text{ has }|U\cap A|=\infty\}.
\]
Set \(S=D_{\omega}(X)\). For each \(x\in S\), let
\[
\mathcal F_x=\{A\subseteq X:\text{some open neighbourhood }U\ni x
\text{ has }|U\setminus A|<\infty\}.
\]
Then \(\mathcal F_x\) is a proper free filter on \(X\), and the following conditions are equivalent:

1. For every two subsets \(A,B\subseteq X\),
   \[
   D_{\omega}(A\cap B)=D_{\omega}(A)\cap D_{\omega}(B).
   \]
2. For every \(x\in S\), the filter \(\mathcal F_x\) is an ultrafilter.

If these conditions hold, \(D_{\omega}(A)=\{x\in S:A\in\mathcal F_x\}\), and \(D_{\omega}:\mathcal P(X)\longrightarrow\mathcal P(S)\) is a Boolean-algebra homomorphism (where its codomain complement is taken inside \(S\)).

This classification has a sharp countability boundary: **on every first-countable space** the two conditions hold if and only if \(S=\varnothing\), equivalently \(D_{\omega}\) vanishes identically. **In ZFC** there nevertheless exists a countably infinite, Hausdorff, zero-dimensional space with \(S\ne\varnothing\) for which both conditions hold. Thus first countability cannot be replaced by countability, Hausdorffness, or zero-dimensionality.

## Assumptions and scope

The statement concerns all topological spaces, without separation, compactness, cardinality, or metrizability hypotheses. The neighbourhoods in the definition can be taken open; all valuations are arbitrary subsets. The symbol \(|U\cap A|=\infty\) means that the intersection is not finite, not that it has any specified infinite cardinality. A proper filter excludes the empty set; it is *free* when its total intersection is empty. The last existence statement uses the ordinary ultrafilter lemma, available in ZFC; no ZF-only existence assertion is made. The result is about the specific \(\omega\)-accumulation operator, not ordinary closure or the Cantor derivative.

The modal reading is exact validity, on a fixed topological space, of
\[
\Diamond_{\omega}(p\land q)\leftrightarrow
(\Diamond_{\omega}p\land\Diamond_{\omega}q)
\]
under every valuation of \(p\) and \(q\).

## Proof

**1. Basic properties.** The operator is monotone and \(D_{\omega}(\varnothing)=\varnothing\). It preserves binary unions. Indeed, the inclusion from right to left is immediate. If \(x\notin D_{\omega}(A)\) and \(x\notin D_{\omega}(B)\), there are neighbourhoods \(U,V\) of \(x\) meeting \(A,B\), respectively, in finite sets. The neighbourhood \(U\cap V\) meets \(A\cup B\) in a finite set, so \(x\notin D_{\omega}(A\cup B)\). Furthermore, \(D_{\omega}(A)\subseteq S\) for every \(A\).

**2. Filter and complement identity.** Fix \(x\in S\). Every neighbourhood of \(x\) is infinite, so \(\varnothing\notin\mathcal F_x\). Upward closure is immediate. If \(A,B\in\mathcal F_x\), choose neighbourhoods \(U,V\) for which \(U\setminus A\) and \(V\setminus B\) are finite. The difference \((U\cap V)\setminus(A\cap B)\) is finite, so \(A\cap B\in\mathcal F_x\). Every cofinite subset of \(X\) belongs to \(\mathcal F_x\); hence its intersection is empty. Therefore \(\mathcal F_x\) is a proper free filter. Directly from the definitions, for all \(A\subseteq X\),
\[
x\notin D_{\omega}(A)\quad\Longleftrightarrow\quad X\setminus A\in\mathcal F_x.
\tag{1}
\]

**3. Sufficiency.** Assume every \(\mathcal F_x\), \(x\in S\), is an ultrafilter. Exactly one of \(A\) and its complement belongs to \(\mathcal F_x\). Applying (1) to the complement gives \(x\in D_{\omega}(A)\) precisely when \(A\in\mathcal F_x\). Since a filter contains \(A\cap B\) exactly when it contains both \(A\) and \(B\), the asserted intersection identity follows. The same argument, together with step 1, proves that the map into \(\mathcal P(S)\) preserves unions, intersections, the bottom, the top, and complements relative to \(S\).

**4. Necessity.** Suppose the intersection identity holds. Fix \(x\in S\), and write \(\mathcal P_x=\{A\subseteq X:x\in D_{\omega}(A)\}\). Because \(D_{\omega}\) preserves intersections and is monotone, \(\mathcal P_x\) is a proper filter, and it contains \(X\). For any \(A\subseteq X\), union preservation gives \(x\in D_{\omega}(A)\cup D_{\omega}(X\setminus A)\), whereas intersection preservation and \(D_{\omega}(\varnothing)=\varnothing\) show these two alternatives cannot both hold. Hence \(\mathcal P_x\) is an ultrafilter. By (1), \(X\setminus A\in\mathcal F_x\) exactly when \(A\notin\mathcal P_x\), and by ultrafilter dichotomy this is equivalent to \(X\setminus A\in\mathcal P_x\). Thus \(\mathcal F_x=\mathcal P_x\) is an ultrafilter.

**5. First-countability obstruction.** Suppose \(X\) is first countable and \(x\in S\). Choose a decreasing countable neighbourhood base \((U_n)_{n\ge0}\) at \(x\). Each \(U_n\) is infinite. Recursively select distinct points \(a_n,b_n\in U_n\), with all selected points pairwise distinct. The disjoint sets \(A=\{a_n:n\ge0\}\) and \(B=\{b_n:n\ge0\}\) meet every neighbourhood of \(x\) infinitely often, because every such neighbourhood contains some \(U_n\), and hence every subsequent \(U_k\). Thus \(x\in D_{\omega}(A)\cap D_{\omega}(B)\), while \(D_{\omega}(A\cap B)=\varnothing\). Intersection preservation fails. If \(S=\varnothing\), monotonicity gives \(D_{\omega}(A)=\varnothing\) for every \(A\), and preservation is automatic.

**6. Sharp Hausdorff example.** In ZFC choose a free ultrafilter \(\mathcal U\) on \(\mathbb N\), and let \(X=\mathbb N\cup\{p\}\) where \(p\notin\mathbb N\). Declare each natural number isolated and take the neighbourhood base at \(p\) to be \(\{p\}\cup U\) for \(U\in\mathcal U\). The filter axioms make this a topology. The space is Hausdorff: for any \(n\), \(\{n\}\) and \(\{p\}\cup(\mathbb N\setminus\{n\})\) are disjoint open neighbourhoods. Every displayed basic neighbourhood of \(p\) is clopen, since its complement lies in the discrete subset \(\mathbb N\). Isolated singletons are clopen as well, proving zero-dimensionality. The only point in \(S\) is \(p\). For any \(A\subseteq X\),
\[
D_{\omega}(A)=\begin{cases}
\{p\},&A\cap\mathbb N\in\mathcal U,\\
\varnothing,&A\cap\mathbb N\notin\mathcal U.
\end{cases}
\]
Indeed, every ultrafilter member has infinite intersection with every ultrafilter member; if \(A\cap\mathbb N\notin\mathcal U\), its complement lies in \(\mathcal U\), giving a neighbourhood with at most one point of \(A\). The ultrafilter intersection law now gives the desired nontrivial conjunction preservation. The obstruction in step 5 also proves the example is not first countable at \(p\).

## Verification

The proof is independent of numerical search. A standalone Python 3 checker, `verify.py`, checks the finite Boolean-filter abstraction behind steps 3 and 4. It enumerates every proper filter on labelled sets of sizes \(1\) through \(5\), and tests all ordered pairs of valuations for union and intersection identities: **57 filters and 36,084 valuation-pair checks**. The infinite filter construction, the first-countability diagonal, and the unrestricted topological theorem are established by the above arguments, not by the finite checker. Run `python3 verify.py` using only the Python standard library.

## Relationship to prior work

Montacute's 2026 *Halo Semantics for Modal Logic*, arXiv:2606.31885, Theorem 6.4 identifies the purely nonstandard halo modality with this \(\omega\)-accumulation operation, and its later modal sections establish other laws and completeness results. The inspected article supplies the operator and its finite-union behavior, but does not give the neighbourhood-ultrafilter characterization, the first-countability boundary, or the Hausdorff example. The filter dichotomy and the free-ultrafilter point construction use standard facts of Boolean algebra and general topology; those isolated facts are not claimed as new. The contribution is the exact operator/frame correspondence and its sharp topological separation.

A related earlier result on the *countable indiscrete* halo space determines its modal validities and non-Kripke representability, not whether the operator distributes over intersections on **all** valuations or the present ultrafilter-topology classification. Searches for alternative ultrafilter, Boolean-homomorphism, and conjunction-preservation formulations did not identify an equivalent full classification, but search absence is not a proof of priority.

## Limitations

The existence example assumes ZFC (or, more specifically, a free ultrafilter on a countably infinite set), and no independence or ZF-only existence theorem is asserted. The theorem classifies one fixed operator law; it does not characterize the full modal logic of all such spaces, establish a global completeness theorem, or claim a new ultrafilter lemma. General ultrafilter duality could yield parts of the proof in alternative notation, so previously published equivalent formulations remain a live originality risk. The finite checker cannot certify the infinite statements. The conclusions have been reviewed internally for mathematical consistency but have not received independent validation.

## References

1. Yoàv Montacute, *Halo Semantics for Modal Logic* (2026), arXiv:2606.31885, originally submitted 2026-06-30; especially Definition 6.2 and Theorem 6.4. https://arxiv.org/abs/2606.31885
2. S. Bardyla, J. Cancino-Manríquez, V. Fischer and C. B. Switzer, *Filters, Ideal Independence and Ideal Mrówka* (2024), background on free filters and pseudointersections. https://www.logic.univie.ac.at/~vfischer/Filters_IdealIndependence_idealMrowka.pdf
