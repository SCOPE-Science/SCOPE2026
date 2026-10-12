# A singleton-or-principal criterion for converse mixing in finite monotone neighborhood products

## Finding

Let \(X,Y\) be finite nonempty sets, with proper monotone local neighborhood families \(\mathcal F\) on \(X\) and \(\mathcal G\) on \(Y\): each is a nonempty upward-closed family of **nonempty** subsets. Write \(\min\mathcal F\) for its antichain of inclusion-minimal neighborhoods, and set
\[
S(\mathcal F)\iff(\forall U\in\min\mathcal F)\ |U|=1,
\qquad P(\mathcal F)\iff |\min\mathcal F|=1.
\]
At the corresponding point of the full product, let \(\Box_1,\Box_2\) be the horizontal and vertical neighborhood modalities and \(\Box_\times\) the rectangle-generated modality. Then, **for every Boolean valuation**,
\[
\Box_1\Box_2p\to\Box_\times p
\quad\Longleftrightarrow\quad S(\mathcal F)\ \lor\ P(\mathcal G),
\]
where the equivalence on the left means validity for all valuations at that point. Dually,
\[
\Box_2\Box_1p\to\Box_\times p
\quad\Longleftrightarrow\quad S(\mathcal G)\ \lor\ P(\mathcal F).
\]
The forward mixing implication from \(\Box_\times p\) to both iterated modalities always holds. The statement applies pointwise to arbitrary finite monotone neighborhood frames, so global validity amounts to the displayed conditions at every product point.

There is an exact local-family census. Let \(D_n\) be the number of antichains of the Boolean lattice of an \(n\)-element set (the Dedekind number), and put \(T_n=D_n-2\) and \(q_n=2^n-1\). Among all \(T_nT_m\) ordered pairs of proper monotone neighborhood families on fixed labeled carriers of respective sizes \(n,m\), exactly
\[
q_nT_m+T_nq_m-q_nq_m
\]
satisfy the first converse, and exactly
\[
T_nT_m-2(T_n-q_n)(T_m-q_m)
 +(T_n-2q_n+n)(T_m-2q_m+m)
\]
satisfy **both** converses. On two three-point carriers these counts are \(203\) and \(131\), respectively, out of \(324\) pairs. Failure of both converses (possibly with different valuations) requires at least three points in each factor, and this lower bound is attained.

## Assumptions and scope

No finite-intersection closure is imposed: this is **monotone, potentially non-normal** neighborhood semantics. Every local family is nonempty, upward closed, and excludes the empty neighborhood. These exclusions matter; empty or inconsistent neighborhood families are not covered. All propositional valuations on \(X\times Y\) are allowed. The theorem is finite-carrier only; nonprincipal infinite filters require different analysis.

For \(A\subseteq X\times Y\), let \(A_x=\{y:(x,y)\in A\}\) and \(A^y=\{x:(x,y)\in A\}\). The three local truth conditions are
\[
\begin{aligned}
\Box_\times(A)&\iff \exists U\in\mathcal F\,\exists V\in\mathcal G\ (U\times V\subseteq A),\\
\Box_1\Box_2(A)&\iff \{x:A_x\in\mathcal G\}\in\mathcal F,\\
\Box_2\Box_1(A)&\iff \{y:A^y\in\mathcal F\}\in\mathcal G.
\end{aligned}
\]

## Proof

**Forward mixing.** If \(U\times V\subseteq A\) for \(U\in\mathcal F\), \(V\in\mathcal G\), each row \(A_x\), for \(x\in U\), contains \(V\), so is in \(\mathcal G\). Upward closure of \(\mathcal F\) gives \(\Box_1\Box_2(A)\). The other order is symmetric.

**First converse, sufficient conditions.** Suppose \(\Box_1\Box_2(A)\). Let \(H=\{x:A_x\in\mathcal G\}\), so \(H\in\mathcal F\). If \(S(\mathcal F)\), some minimal singleton neighborhood \(\{x\}\) is contained in \(H\); hence \(\{x\}\times A_x\subseteq A\) is a permitted rectangle. If \(P(\mathcal G)\), let \(V_0\) be its unique minimal member; every \(A_x\in\mathcal G\) contains \(V_0\). Hence \(H\times V_0\subseteq A\) is a permitted rectangle. Thus either condition implies the converse.

**First converse, necessity.** Suppose neither \(S(\mathcal F)\) nor \(P(\mathcal G)\). Choose an inclusion-minimal \(U\in\mathcal F\) with at least two elements, and distinct minimal \(V_0,V_1\in\mathcal G\). Choose \(u_0\in U\). Form \(A\) whose row at \(u_0\) is exactly \(V_0\), whose rows at the other points of \(U\) are exactly \(V_1\), and whose rows outside \(U\) are empty. The set of \(\mathcal G\)-good rows is precisely \(U\), so \(\Box_1\Box_2(A)\) holds. If a permitted rectangle \(U'\times V'\subseteq A\) existed, nonemptiness of \(V'\) would give \(U'\subseteq U\). Minimality of \(U\) forces \(U'=U\); therefore \(V'\subseteq V_0\cap V_1\). But distinct minimal members of an upward-closed family cannot have an admitted subset in their intersection. Contradiction. Interchanging the two factors establishes the second equivalence.

**Counting.** Proper monotone families correspond bijectively to nonempty antichains of nonempty subsets; there are \(T_n=D_n-2\). The families with only singleton minimal members are the nonempty selections of singletons, numbering \(q_n=2^n-1\). Families having exactly one minimal member also number \(q_n\). Their intersection consists of the \(n\) singleton principal families. Inclusion-exclusion gives the first census. Failure of the first converse requires a non-singleton-generated first family and a nonprincipal second family; failure of the second is its transpose. Their intersection requires **both** families to lie outside both special classes, of cardinalities \(T_n-2q_n+n\) and \(T_m-2q_m+m\). Inclusion-exclusion gives the second census.

For carrier sizes one and two, every proper monotone family is singleton-generated or principal. On a three-element set, the antichain \(\{\{0,1\},\{0,2\}\}\) is neither. Taking this antichain in both factors proves the sharp two-order obstruction threshold.

## Verification

Run `python3 verify.py` with Python 3.10 or later. The checker independently generates every proper monotone local family on labeled sets of size one, two, or three, evaluates every Boolean subset of each Cartesian product, and compares the semantic equations against both structural criteria and the counting formulas. It checks \(529\) ordered local-family pairs and \(175682\) pair/valuation cases, and reproduces the \((3,3)\) counts \(203,131\). These finite tests support but do not replace the unrestricted finite-size proof above.

## Relationship to prior work

Aghamov, Kudinov, Nguyen, and Piribauer (2026) introduce the horizontal, vertical, and rectangle-generated modalities on **normal filter** neighborhood products and establish the forward mixing principle, among broader axiomatization results. Sano (2011) axiomatizes two-dimensional hybrid products of **monotone** neighborhood frames, with horizontal and vertical operators, but does not introduce this third rectangle modality. Kudinov (2014) analyzes products of **normal** neighborhood frames. The present criterion concerns converse mixing with the third modality after dropping finite-intersection closure; it therefore does not assert novelty for the finite normal-filter subcase, where local filters are principal. Classical Dedekind numbers and elementary antichain enumeration are inputs, not novel sequences themselves.

## Limitations

No completeness theorem or axiomatization for the full non-normal product logic is claimed. No infinite-carrier dichotomy is claimed. The structural classification is only for local proper monotone families; no numerical census of globally assigned frame structures is asserted. An older equivalent characterization from monotone modal, Boolean-function, or hypergraph literature remains possible.

## References

1. R. Aghamov, A. Kudinov, M. T. Nguyen, and J. Piribauer, *On Modal Logics of Full Products of Neighborhood Frames*, Electronic Proceedings in Theoretical Computer Science 447 (2026), 1–15, DOI: 10.4204/EPTCS.447.1; arXiv:2606.31852.
2. K. Sano, *Axiomatizing Hybrid Products of Monotone Neighborhood Frames*, Electronic Notes in Theoretical Computer Science 273 (2011), 51–67, DOI: 10.1016/j.entcs.2011.06.012.
3. A. Kudinov, *Neighbourhood Frame Product KxK*, Advances in Modal Logic 10 (2014).
4. R. Dedekind, *Über Zerlegungen von Zahlen durch ihre grössten gemeinsamen Teiler*, Festschrift Hoch. Braunschweig (1897), 1–40 (classical antichain counts).
