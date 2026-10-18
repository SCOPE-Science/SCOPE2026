# The one-world price of nonvacuism: Boolean rank of parallel counterpossibles

## Finding

Fix integers \(r,s\geq 1\). For distinct atoms \(p_1,\ldots,p_r,q_1,\ldots,q_s\), let \(\alpha_i=\neg(p_i\to p_i)\), which is false at every classical world. For any prescribed matrix \(T\in\{0,1\}^{r\times s}\), consider models with exactly one logic-normal world \(w\), all \(q_j\) true at \(w\), and
\[
T_{ij}=1\quad\Longleftrightarrow\quad w\Vdash\alpha_i>q_j.
\]
In the selection-function semantics of Huang and Wen, let \(b_{\mathrm{SCP}}(T)\) and \(b_{\mathrm{SCP1}}(T)\) be the smallest possible number of anti-logical worlds in a finite model of the respective system satisfying all these requirements. Write \(B=\mathbf1-T\), and let \(\rho(B)\) denote its **Boolean rank**, the minimum nonnegative integer \(k\) such that
\[
B_{ij}=\bigvee_{t=1}^{k}\left(A_{it}\land C_{tj}\right)
\]
for two binary matrices \(A,C\), with an empty disjunction defined to be false.

**Theorem (sharp nonvacuity budget).** For every such matrix,
\[
\boxed{b_{\mathrm{SCP}}(T)=\rho(B),\qquad
b_{\mathrm{SCP1}}(T)=\rho(B)+\mathbf1\{\exists i\ \forall j\ T_{ij}=1\}.}
\]
Moreover, the exact worst-case budgets are
\[
\boxed{\max_T b_{\mathrm{SCP}}(T)=\min(r,s),\qquad
\max_T b_{\mathrm{SCP1}}(T)=\min(r,s+1).}
\]
The Boolean-rank invariant itself is classical. The claim is the exact interpretation of this invariant as the minimum size of the anti-logical domain under *both* modal-conditional semantic systems, including the discrete extra-world cost of the universally quantified nonempty-selection requirement.

## Assumptions and scope

The logic's formulas are built from atoms, negation, implication, two modal boxes and the conditional \(>\). A model is \((W,N,R_M,R_L,f,V)\), where \(N\subseteq W\), \(I=W\setminus N\), and \(R_M,R_L\) are equivalence relations on \(N\), with \(R_M(w)\subseteq R_L(w)\). The selection \(f(w,\varphi)\subseteq W\) is indexed by the *syntactic formula* \(\varphi\). At normal worlds Boolean and modal truth are classical and \(w\Vdash\varphi>\psi\) precisely when \(f(w,\varphi)\subseteq[\![\psi]\!]\). At anti-logical worlds \(z\), each full formula may receive an independent truth value through \(V\). The constraints are: (id) \(f(w,\varphi)\subseteq[\![\varphi]\!]\); (soc-m) if \(\Diamond_M\varphi\) at \(w\), then \(f(w,\varphi)\subseteq R_M(w)\); (sic) if \(\Diamond_L\varphi\) at \(w\), then \(f(w,\varphi)\subseteq N\). SCP1 adds (rl) \(R_L(w)=N\) and (ne) \(f(w,\varphi)\ne\varnothing\) for *all* normal worlds and all formulas. These are the exact semantic definitions in the cited motivating work.

Only a single normal world is allowed here; necessarily \(R_M=R_L=\{(w,w)\}\), which satisfies (rl). The consequent atoms \(q_j\) must be true at \(w\). The contradictory antecedents \(\alpha_i\) are distinct formulas, even though they are logically equivalent at normal worlds. The result is *not* asserted for semantic variants imposing extensionality of selections under equivalence of antecedents, nor for extra constraints on the anti-logical valuation.

## Proof

**1. All selected witnesses of a contradiction are anti-logical.** For each \(i\), classical truth gives \(w\not\Vdash\alpha_i\). By (id), \(f(w,\alpha_i)\subseteq I\). For an anti-logical world \(z\), define the set of failed consequents
\[
S_z=\{j\in\{1,\ldots,s\}:z\not\Vdash q_j\}.
\]
Let \(F_i=f(w,\alpha_i)\). Since all \(q_j\) hold at the normal world, conditional truth is equivalent to
\[
\{j:B_{ij}=1\}=\bigcup_{z\in F_i}S_z.
\]
Thus any model with \(k\) anti-logical worlds induces a Boolean factorization of \(B\) with \(k\) factors, by setting \(A_{iz}=\mathbf1\{z\in F_i\}\) and \(C_{zj}=\mathbf1\{j\in S_z\}\). Necessarily \(k\ge\rho(B)\).

**2. An all-true row costs one world in SCP1.** If some row of \(T\) is entirely true, then the corresponding \(B\)-row is zero. In SCP1, \(F_i\ne\varnothing\) by (ne). Every \(z\in F_i\) satisfies *every* consequent \(q_j\), so its corresponding row \(C_z\) is the zero vector. Erasing this factor still represents \(B\). Consequently, \(\rho(B)\le k-1\). No such restriction is imposed in SCP, where \(F_i=\varnothing\) is permitted.

**3. Realizing a factorization in a complete semantic model.** Fix any Boolean factorization of rank \(k=\rho(B)\). Introduce one normal world \(w\), and \(k\) anti-logical worlds \(z_1,\ldots,z_k\). Give each \(q_j\) truth at \(w\), and arrange at \(z_t\) that \(q_j\) is false exactly when \(C_{tj}=1\). Make \(\alpha_i\) true at every anti-logical world, independently of any other syntactic formulas, as allowed by the non-recursive anti-logical valuation. Choose
\[
f(w,\alpha_i)=\{z_t:A_{it}=1\}.
\]
This selection realizes exactly \(T\). For SCP1, if \(B\) has a zero row, append a new anti-world \(z_0\) satisfying all \(q_j\) and use \(\{z_0\}\) for each zero row. For every nonzero row, the factorization already supplies at least one selected world. When \(B\) has no zero row, no extra world is needed. (In SCP the selection for a zero row can remain empty.)

It remains crucial to extend the finitely prescribed selections to *every other formula*, satisfying the global constraints. Declare all formulas at each anti-world true except those consequent atoms \(q_j\) assigned false above. This is legitimate even for negations and implications because anti-logical truth is non-compositional; in particular all \(\alpha_i\) are true there. Assign arbitrary truth to the \(p_i\) at \(w\) and set all \(q_j\) true there. Build the remaining selection function inductively on syntactic formula complexity: once truth of a formula \(\varphi\) at \(w\) is determined from its proper subformulas and their selections, put \(f(w,\varphi)=\{w\}\) if it is true. Otherwise put \(f(w,\varphi)=\varnothing\) for SCP, or select an arbitrary fixed anti-world \(z_*\) in SCP1. The choices prescribed for \(\alpha_i\) take precedence; their truth at \(w\) is false independently of selections. In SCP1 at least one anti-world exists: if \(B\) has a nonzero row then \(k\ge1\), while if it has no nonzero rows the appended \(z_0\) exists. All other formulas false at \(w\) are true at \(z_*\): the only anti-world exceptions are the \(q_j\), all true at \(w\). Hence (id), (soc-m), (sic) hold for all formulas; (ne) holds in SCP1. Modal accessibility is diagonal, satisfying (rl). Well-foundedness follows because evaluating a formula's conditional subexpressions consults selections for strictly smaller antecedent formulas. This realizes the lower bounds without unverified assumptions about the remaining language.

**4. Sharp maxima.** Boolean rank satisfies \(\rho(B)\le\min(r,s)\); an embedded identity matrix attains equality. If \(B\) has a zero row, its Boolean rank is at most \(\min(r-1,s)\), so the SCP1 formula yields \(b_{\mathrm{SCP1}}\le\min(r,s+1)\); without a zero row the same bound follows from \(\rho(B)\le\min(r,s)\). To attain the SCP1 maximum, set the first row of \(B\) to zero, use \(\min(r-1,s)\) distinct unit rows, and repeat rows if necessary. Every unit row requires its own factor, so \(\rho(B)=\min(r-1,s)\), and (ne) forces exactly one additional all-true anti-world. This proves both sharp formulas for all positive \(r,s\).

## Verification

The supplied `check.py` brute-forces the two types of subset-union bases for every binary table of dimensions \(1\le r\le4\), \(1\le s\le3\): **5,050 tables**. It confirms both the Boolean-rank identity and the exact worst-case SCP1 bound. A separate loop tests sharpness constructions for 196 parameter pairs with \(1\le r,s\le14\). A direct semantic truth-table reproduction tests 682 finite instances with \(1\le r,s\le3\). Its output is deterministic and uses Python's standard library only: run `python3 check.py`. These finite checks are not a proof of the quantified theorem; the previous four arguments establish it.

## Relationship to prior work

Huang and Wen (2026, Definitions 3.2–3.5 and 4.1) supply the semantic constraints and prove soundness, completeness and decidability of SCP/SCP1. Their conclusion explicitly treats the richness of the anti-logical domain as a question but does not calculate a minimum number of such worlds for arbitrary simultaneous counterpossibles. Their nonempty-selection rule is exactly the hypothesis producing the one-world surcharge here.

Boolean matrix rank, Boolean factorization, and equivalence to covering the ones by bicliques are classical (see Geraci, Kunin and Seceleanu, 2025). Neither Boolean rank nor its usual upper bound is claimed as new. The mathematical contribution is the full SCP/SCP1 realization equivalence, which includes extension of finitely prescribed counterpossible selections to a legal selection for every formula, and the sharp difference between the two systems. Published discussions of impossible-world semantics (e.g. Berto and Jago) motivate nonvacuous counterpossibles but do not state this exact finite witness-budget theorem.

## Limitations

The result uses one normal world, propositional contradictory antecedents indexed *syntactically*, and freely assigned anti-logical truth values as allowed by the specified model class. Formula equivalence is not quotiented in the selection argument; imposing an additional antecedent-extensionality axiom changes the problem. The result counts worlds, not formula length or computational time. The standard Boolean-rank facts are prior art, and a specialized equivalent semantic resource result could exist under another terminology. The finite checker corroborates, but cannot certify, the general mathematical proof. Independent external verification has not occurred.

## References

1. Chen Huang and Xuefeng Wen, *Stratified Counterpossible Logic*, EPTCS 447 (2026), 500–517, doi:10.4204/EPTCS.447.28, first arXiv posting June 30, 2026, arXiv:2606.31881. Primary text consulted for Definitions 3.1–3.5, Section 4 and the concluding discussion.
2. Juliann Geraci, Alexander B. Kunin and Alexandra Seceleanu, *Boolean Rank via Monomial Ideals* (2025), arXiv:2509.09570, for the standard Boolean-rank/biclique-cover equivalence.
3. Francesco Berto and Mark Jago, *Impossible Worlds*, Stanford Encyclopedia of Philosophy, https://plato.stanford.edu/entries/impossible-worlds/, for nonvacuist semantic context.
