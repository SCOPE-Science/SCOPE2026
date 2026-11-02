# Single-agent coalition algebras: a Dedekind-number normal form and four exact censuses

## Finding
Fix an integer \(n\ge1\) and the labelled Boolean algebra \(B=\mathcal P(W)\), where \(W=\{1,\ldots,n\}\). For the single-agent language with coalitions \(\varnothing\) and \(\{a\}\), define \(M(k)\) to be the number of monotone Boolean functions on \(k\) variables (the \(k\)-th Dedekind number), and put
\[
Q_n=1+\sum_{k=1}^{n}\binom nk\bigl(M(k)-2\bigr).
\]
The numbers of ordered pairs of unary operations \((f_{\varnothing},f_a)\) on this **fixed labelled** Boolean algebra satisfying respectively the minimal coalition algebra axioms, these axioms plus seriality, these axioms plus determinism, and these axioms plus both conditions are exactly
\[
\boxed{Q_n^n,\quad (Q_n-1)^n,\quad 2^{n^2},\quad (2^n-1)^n.}
\]
The independence-of-agents axiom is already valid for a single agent, so these are all four distinct basic axiom families in that signature (as families of expansions for sufficiently large carriers). For \(n=1,2,3,4\) the four counts, in the same order, are \((2,1,2,1)\), \((49,36,16,9)\), \((39304,35937,512,343)\), and \((5082121521,5006411536,65536,50625)\).

## Assumptions and scope
The Boolean algebra has exactly \(n\) individually labelled atoms. For both \(C\in\{\varnothing,\{a\}\}\), the basic equations are
\[
 f_C(0)=0,\qquad f_{\varnothing}(x)\le f_a(x),\qquad f_C(x)\le f_{\varnothing}(1),
\]
\[
 f_{\varnothing}(\neg x\vee y)\wedge f_C(x)\le f_C(y)\quad\text{for all }x,y\in B.
\]
Seriality means \(f_C(1)=1\) for each coalition. Determinism means
\[
 f_C(x\vee y)\le f_C(x)\vee f_a(y)\quad\text{for both coalitions and every }x,y\in B.
\]
The independence axiom means \(f_C(x)\wedge f_D(y)\le f_{C\cup D}(x\wedge y)\) whenever \(C\cap D=\varnothing\). No assertions are made about larger agent sets, unlabelled isomorphism classes, or the lattice of all intermediate logics.

## Proof
All inequalities in \(B=\mathcal P(W)\) can be checked at a single output atom \(s\in W\), and choices at different output atoms are independent. Write \(e(s)=1\) if and only if \(s\in f_{\varnothing}(W)\). If \(e(s)=0\), the upper-bound axiom \(f_C(x)\le f_{\varnothing}(1)\) forces both coordinate outputs to vanish for every input.

Suppose \(e(s)=1\). The mixed implication axiom makes each coordinate monotone: for \(X\subseteq Y\), \(\neg X\cup Y=W\), hence \(s\in f_C(X)\Rightarrow s\in f_C(Y)\). It also makes \(f_{\varnothing}\) preserve binary intersections at \(s\): since \(Y\subseteq\neg X\cup(X\cap Y)\), monotonicity gives
\[
 s\in f_{\varnothing}(X)\cap f_{\varnothing}(Y)\Rightarrow s\in f_{\varnothing}(\neg X\cup(X\cap Y))\cap f_{\varnothing}(X)\Rightarrow s\in f_{\varnothing}(X\cap Y).
\]
The reverse implication follows by monotonicity. Together with \(s\notin f_{\varnothing}(\varnothing)\) and \(s\in f_{\varnothing}(W)\), the inputs whose empty-coalition image contains \(s\) form a proper filter of the **finite** Boolean lattice \(\mathcal P(W)\). Therefore there is a unique nonempty subset \(T_s\subseteq W\) such that
\[
 s\in f_{\varnothing}(X)\quad\Longleftrightarrow\quad T_s\subseteq X.
\]

The mixed implication with \(C=\{a\}\) says that, whenever \(X\cap T_s\subseteq Y\), membership \(s\in f_a(X)\) implies \(s\in f_a(Y)\), because \(T_s\subseteq\neg X\cup Y\). In particular, it depends only on \(X\cap T_s\). It is thus a monotone map \(w_s:\mathcal P(T_s)\to\{0,1\}\). The axioms \(f_a(0)=0\) and \(f_{\varnothing}(X)\le f_a(X)\) give \(w_s(\varnothing)=0\) and \(w_s(T_s)=1\). Conversely, any nonempty \(T_s\) together with any such monotone \(w_s\), or an inactive state with both coordinate maps zero, satisfies *all* the basic equations: the mixed implication follows directly from inclusion of traces in \(T_s\). This is a unique coordinatewise normal form.

For \(|T_s|=k\), there are exactly \(M(k)-2\) monotone Boolean functions with the prescribed distinct endpoint values: every nonconstant monotone Boolean function has those endpoints, and the only two excluded functions are the two constants. Hence there are \(Q_n\) independent choices per output atom. Seriality excludes exactly the one inactive choice per atom, yielding \((Q_n-1)^n\).

Now impose determinism. Fix any active coordinate, with nonempty \(T_s\). For every \(t\in T_s\), set \(X=T_s\setminus\{t\}\) and \(Y=\{t\}\). The determinism instance with \(C=\varnothing\) has \(s\in f_{\varnothing}(X\cup Y)\) but \(s\notin f_{\varnothing}(X)\), and therefore forces \(w_s(\{t\})=1\). By monotonicity and \(w_s(\varnothing)=0\), the only possibility is
\[
 w_s(U)=1\quad\Longleftrightarrow\quad U\ne\varnothing.
\]
Conversely this disjunction map satisfies determinism for \(C=a\) by union preservation and for \(C=\varnothing\) because \(T_s\subseteq X\cup Y\) with \(T_s\not\subseteq X\) entails \(Y\cap T_s\ne\varnothing\). Thus each active coordinate has exactly \(2^n-1\) deterministic choices of \(T_s\), plus one inactive choice, giving \((2^n)^n\), and seriality additionally deletes the inactive option, giving \((2^n-1)^n\).

Finally, independence is automatic. The only disjoint pairs of coalitions are \((\varnothing,\varnothing)\), \((\varnothing,a)\), and \((a,\varnothing)\). In the active normal form, if \(T_s\subseteq X\), then the traces of \(Y\) and \(X\cap Y\) coincide, so \(s\in f_a(Y)\Rightarrow s\in f_a(X\cap Y)\); for two empty coalitions, the principal filter preserves intersections. At inactive coordinates all conclusions are vacuous. These verify every independence instance. \(\square\)

## Verification
A standalone exhaustive checker (`checker.py`) enumerates every pair of unary operations on Boolean algebras with one and two labelled atoms, tests the defining equations and the seriality and determinism instances, and returns the exact four counts shown above. For three and four atoms the displayed values follow by substituting the known Dedekind values \(M(1)=3,M(2)=6,M(3)=20,M(4)=168\) into the proved formula; these larger cases are **not** exhaustively enumerated by the checker. Full enumeration on two atoms checks \(4^6=4096\) pairs respecting zero preservation; this is finite corroboration, not a proof for arbitrary \(n\).

## Relationship to prior work
Wang and Dou (2026), *The Lattice of Coalition Logics between MCL and CL: Coatoms and Compact Meets*, defines the Boolean coalition algebra axioms, studies at least two agents, and derives general structural extension-lattice results; it does not enumerate the omitted one-agent finite expansions. Li and Ju (2024) introduce minimal coalition logic and its strategic semantics, while their complementary study establishes completeness for optional seriality, independence and determinism. The Dedekind numbers and their antichain interpretation are classical. The present statement is a restricted one-agent **enumeration and unique normal form**, not a new proof of the general algebraic correspondence, the older completeness theorems or any new lattice coatom result.

## Limitations
Counts are for labelled Boolean reducts and distinct operator pairs, not isomorphism types of algebras or action presentations. The normal form exploits finite principal filters; it does not extend unchanged to infinite atom sets. Historical priority for an equivalent one-agent effectivity-function census in older strategic-logic literature is not independently certified.

## References
1. Shanxia Wang and Yuqiang Dou, *The Lattice of Coalition Logics between MCL and CL: Coatoms and Compact Meets*, arXiv:2610.24466v1, first public October 17, 2026, Sections 2–3 and 7. https://arxiv.org/html/2610.24466v1
2. Yinfeng Li and Fengkui Ju, *A minimal coalition logic*, arXiv:2403.14704v3 (first public March 17, 2024), Sections 5–6. https://arxiv.org/html/2403.14704v3
3. Yinfeng Li and Fengkui Ju, *Completeness of coalition logics with seriality, independence of agents, or determinism*, arXiv:2409.14635, first public September 23, 2024. https://arxiv.org/abs/2409.14635
4. Tamon Stephen and Timothy Yusun, *Counting inequivalent monotone Boolean functions*, arXiv:1209.4623, first public September 20, 2012. https://arxiv.org/abs/1209.4623
