# Sharp agreement spectra for the implication-only fragment of classical propositional logic

## Finding
Consider the implication-only fragment of classical propositional logic, with the standard material conditional \(a\to b=\neg a\lor b\). Formulas are built from propositional variables and \(\to\) only, with no primitive constants, conjunction, or negation. The semantic-agreement probability of two formulas is the fraction of uniformly random Boolean assignments on which they have equal truth values. Equivalently, these are equations in the two-element algebra \(\mathbf I=(\{0,1\},\to)\). Then
\[
\operatorname{PSpec}(\mathbf I)=\mathbb Z[1/2]\cap[1/4,1].
\]
More sharply, for every integer \(n\ge2\), the agreement counts realizable by equations whose union of variables is contained in a fixed \(n\)-element set are exactly the consecutive integers
\[
2^{n-2},\ 2^{n-2}+1,\ldots,\ 2^n.
\]
For \(n=1\) they are \(1\) and \(2\). If an equation ignores some variables from the fixed \(n\)-element set, those variables are still sampled uniformly; its probability is unchanged.

This resolves, for the material-implication groupoid, the unknown-spectrum entry of the two-element groupoid table in Cardó's 2026 study [1]. The spectrum is countable and dense in the proper interval \([1/4,1]\); its lower endpoint is attained.

## Assumptions and scope
All terms are variable-only terms of the single-sorted signature \(\{\to\}\); an expression such as \(x\to x\) is a term evaluating to \(1\), but \(1\) is **not** an additional primitive symbol. We use an auxiliary notation \(U\lor V:=(U\to V)\to V\); each appearance denotes that specific implication-only term. No restrictions on repeated variables, term depth, or equation length are imposed. There are no independent constants in the language.

For a term \(t\), write \(\rho(t)\) for its rightmost terminal variable: \(\rho(x_i)=x_i\), and \(\rho(u\to v)=\rho(v)\). For an equation \(t\approx s\) in \(n\) variables, its agreement count is \(d_n(t,s)=|\{a\in\{0,1\}^n:t(a)=s(a)\}|\).

## Proof
**1. Universal lower bound.** Structural induction on \(t\) gives
\[
\rho(t)=1\ \Longrightarrow\ t=1,
\]
because the consequent of any implication is enough to force the implication to \(1\). Therefore both sides of \(t\approx s\) equal \(1\) whenever \(\rho(t)=\rho(s)=1\). This occurs on at least one quarter of assignments if the two terminal variables are distinct, and on one half if they coincide. Every equational probability is dyadic. The equation \(x\approx x\to y\) agrees on exactly the assignment \((x,y)=(1,1)\), so the bound \(1/4\) is attained.

**2. Exact truth-count lemma.** For every \(m\ge1\) and integer \(j\) with \(2^{m-1}\le j\le2^m\), there exists an implication-only term \(T_{m,j}\) on at most \(m\) variables with exactly \(j\) true assignments among all \(2^m\) assignments.

For \(m=1\), take \(T_{1,1}=x_1\) and \(T_{1,2}=x_1\to x_1\). If \(m\ge2\) and \(j=2^m\), a tautology works. Otherwise put \(r=2^m-j\), so \(1\le r\le2^{m-1}\). Choose \(1\le\ell\le m-1\) for which \(2^{\ell-1}\le r\le2^\ell\), and by induction take \(A=T_{\ell,r}\) on \(x_1,\ldots,x_\ell\). Define
\[
T_{m,j}=(A\to x_{\ell+1})\lor x_{\ell+2}\lor\cdots\lor x_m,
\]
where each disjunction is replaced by its displayed implication-only expansion. This term is false precisely when \(A=1\) and all of \(x_{\ell+1},\ldots,x_m\) vanish: there are exactly \(r\) such assignments, hence exactly \(j\) true ones. This proves the lemma constructively.

**3. Four explicit families fill every admissible agreement count.** Fix \(n\ge3\), let \(x,y\) be two distinguished independent variables, and let any auxiliary term \(A\) use variables disjoint from those specified below. The truth-count lemma gives every requisite value \(j\).

- **Family I:** \(x\approx(x\to A)\), with \(A\) using the other \(n-1\) variables. If \(A\) has \(j\) true assignments there, the equation has \(d=j\) agreements, giving the interval \([2^{n-2},2^{n-1}]\) of integers.
- **Family II:** \(x\approx((x\to A)\to y)\), with \(A\) using the \(n-2\) variables other than \(x,y\). If \(A\) has \(j\) true assignments, the equation has \(d=3\cdot2^{n-2}-j\) agreements, hence all integers in \([2^{n-1},5\cdot2^{n-3}]\).
- **Family III:** \(x\approx(y\to(A\to x))\), with \(A\) again on \(n-2\) variables. If \(A\) has \(j\) true assignments, then \(d=2^{n-1}+j\), yielding \([5\cdot2^{n-3},3\cdot2^{n-2}]\).
- **Family IV:** \(x\approx(A\to x)\), with \(A\) on the other \(n-1\) variables. Then \(d=2^{n-1}+j\), yielding \([3\cdot2^{n-2},2^n]\).

Each formula follows directly by splitting on \(x=0\) or \(x=1\), and for Families II--III also on \(y\). In Family II the agreement probability is \(3/4-j/2^n\); in Family III it is \(1/2+j/2^n\). The four consecutive intervals meet at endpoints and exhaust the full interval \([2^{n-2},2^n]\).

For \(n=2\), the respective equations \(x\approx(x\to y)\), \(x\approx y\), \(x\approx(y\to x)\), \(x\approx x\) attain \(1,2,3,4\) agreements, respectively. For \(n=1\), \(x\approx x\) and \(x\approx(x\to x)\) attain \(2\) and \(1\).

**4. Spectrum.** Combining step 1 with step 3, every achievable probability is dyadic and at least \(1/4\), and for each \(n\ge2\) every \(d/2^n\) in that interval is achieved. Every dyadic in \([1/4,1]\) has such a denominator after multiplying numerator and denominator by a common power of \(2\), so the asserted spectrum follows. \(\square\)

## Verification
The included standalone pure-Python checker `check_implication_spectrum.py` constructs \(T_{m,j}\) for all feasible \(j\) with \(1\le m\le8\), constructs agreement witnesses for all feasible counts with \(2\le n\le8\), and truth-table checks each witness. Independently, it computes **all** implication-only term functions by fixed-point closure under \(\to\) for arities \(1,2,3,4\), obtaining respectively \(2,6,38,942\) term operations; exhaustive pairwise comparisons give precisely the count ranges in the theorem. Its expected success marker is `IMPLICATION_EQUATIONAL_SPECTRUM_EXACT_OK 651 constructive_checks clone_sizes [2, 6, 38, 942]`. The theorem for unbounded arity is supplied by steps 1--4, not inferred from finite tests.

Run the checker as `python3 check_implication_spectrum.py` using Python 3 with no third-party packages.

## Relationship to prior work
Cardó [1] defines and studies equational probabilities of finite algebras. Its Table 1, Section 4, explicitly records the spectrum of the two-element binary operation with table \((1,1,0,1)\), namely material implication, among the unknown spectra; the nearby semilattice and Sheffer-functionally-complete spectra concern different operations. The present calculation uses only the binary implication reduct and settles that particular table entry. General clone-theoretic and implicational-calculus results motivate the proof, but counting semantic term functions alone does not give the full pairwise-agreement spectrum; the four witness families provide the missing exact realization statement. Cardó [2] classifies groupoids with minimal equational spectra, which do not include the spectrum here because it contains \(1/4\) and infinitely many other values. Independent priority checking against all older literature has not been performed.

## Limitations
The algebra has exactly two elements and exactly one primitive binary operation, material implication. Adding constants or other Boolean operations can change the spectrum. The theorem counts probabilities of satisfaction of *equations*, not the truth-value distribution of an arbitrary formula. It does not classify term equivalence classes or spectra of larger implication algebras. The checker exhausts bounded arities only; the proof is required for the universal quantifiers. No independent scientific audit has been performed.

## References
[1] C. Cardó, *Probabilistic equational spectrum, primality and approximation in finite algebras*, arXiv:2604.08446v1 (first publicly posted 2026-04-09), especially Definition 2.1 and Table 1, Section 4. https://arxiv.org/abs/2604.08446

[2] C. Cardó, *On semigroups and groupoids with minimal probabilistic spectrum*, arXiv:2603.19487 (2026), Sections 2--3. https://arxiv.org/abs/2603.19487
