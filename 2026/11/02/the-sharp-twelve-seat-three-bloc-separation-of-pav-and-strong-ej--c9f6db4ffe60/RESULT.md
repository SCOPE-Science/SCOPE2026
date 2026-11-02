# The sharp twelve-seat three-bloc separation of PAV and strong EJR+ up to one

## Finding

Consider the following approval-election family. The candidates are partitioned into a common block \(A\) of \(r\) candidates, a challenger \(b\), and a competing block \(C\) of \(s\) candidates, where \(r,s\ge1\). There are \(p\) voters approving \(A\cup\{b\}\), \(h\) voters approving exactly \(A\), and \(q\) voters approving \(A\cup C\), where \(p,h,q\) are positive integers. The committee size is \(k=r+s\), and the committee under study is \(W=A\cup C\).

**Theorem.** In this family, \(W\) maximizes the proportional approval voting (PAV) score if and only if
\[
\frac qk\ge\frac p{r+1}.
\]
It is the unique PAV-optimal committee if the inequality is strict. Furthermore, \(W\) satisfies the payment-based *strong EJR+ up to one* axiom of Skowron (2026) if and only if
\[
\frac r{p+h}+\frac1p>\frac{k}{p+h+q}.
\]
Every PAV-optimal \(W\) in this family belongs to the ordinary cooperative core and satisfies standard EJR+.

As a consequence, no PAV-optimal committee in this three-bloc family violates strong EJR+ up to one when \(k\le11\), but for **every** integer \(k\ge12\) there is an election in this family whose **unique** PAV-optimal committee violates the axiom. Specifically, take
\[
r=2,\qquad s=k-2,\qquad p=6,\qquad h=10,\qquad q=2k+1.
\]
For \(k=12\), this yields \(41\) voters, \(13\) candidates, and a violation with an exact payment shortfall of \(1/984\). The twelve-seat minimality is **within the specified three-bloc family only**, not a universal minimum across arbitrary approval elections.

## Assumptions and scope

All candidates have unit cost; the budget is the integer committee size \(k\), with exactly \(k\) winners. Utilities are additive approval utilities, taking values \(0\) or \(1\) per candidate. The electorate contains \(n=p+h+q\) voters and the candidate set has \(m=k+1\) members. All five parameters \(r,s,p,h,q\) are positive integers.

Let \(H_t=\sum_{j=1}^{t}1/j\) for \(t\ge1\), and \(H_0=0\). PAV maximizes \(\sum_i H_{|A_i\cap W|}\), where \(A_i\) is voter \(i\)'s approval set.

For clarity, we spell out the approval-specialized strong EJR+ up-to-one criterion. For each nonwinner \(c\), each nonempty voter group \(S\) with \(\sigma_S(c)>0\), where \(\sigma_S(d)=|\{i\in S:d\in A_i\}|\), there must be a voter \(i\in S\) for whom
\[
\frac{\mathbf1_{c\in A_i}}{\sigma_S(c)}
+\sum_{d\in W\cap A_i}
\min\!\left\{\frac1{\sigma_S(d)},\frac1{\sigma_S(c)}\right\}
>\frac kn.
\]
No division by zero occurs in the sum, since \(i\) approves every summand candidate. The strict inequality is part of the *up-to-one* criterion. The cooperative core rules out any coalition purchasing candidates within its proportional budget and making each member strictly better off.

## Proof

**1. Exact PAV optimality.** Since there are exactly \(k+1\) candidates, every other size-\(k\) committee is obtained by replacing one member of \(W\) with \(b\). If the removed member belongs to \(C\), the score change is
\[
\Delta_C=\frac{p}{r+1}-\frac qk.
\]
If the removed member belongs to \(A\), the \(p\) voters who approve \(b\) preserve their satisfaction count, the \(h\) voters lose their \(r\)-th approved winner, and the \(q\) voters lose their \(k\)-th. The score change is
\[
\Delta_A=-\frac hr-\frac qk<0.
\]
This proves both the optimality condition and the uniqueness assertion.

**2. Exact strong-EJR+ condition.** The sole unelected candidate is \(b\). Fix a group \(S\) with \(x\) voters of type \(A\cup\{b\}\), \(y\) of type \(A\), and \(z\) of type \(A\cup C\). The axiom only requires testing \(x\ge1\). Set \(t=x+y+z\). All selected \(A\)-candidates have \(t\) supporters in \(S\), while \(b\) has \(x\).

If \(z>0\), each voter of type \(A\cup C\) has payment expression
\[
\frac rt+\frac{s}{\max\{x,z\}}.
\]
Because \(x,z>0\), one has \(\max\{x,z\}<t\). Consequently this expression exceeds \(k/t\), and hence exceeds \(k/n\). Such a group cannot witness failure.

If \(z=0\), a voter approving \(b\) has expression \(r/(x+y)+1/x\), and an \(A\)-only voter has expression \(r/(x+y)\). The maximal expression is therefore \(r/(x+y)+1/x\). It is nonincreasing in both \(x\) and \(y\), so the smallest possible maximum over all such groups is attained at \(x=p,y=h\). Failure of the axiom is therefore equivalent to
\[
\frac r{p+h}+\frac1p\le\frac k{p+h+q},
\]
proving the stated if-and-only-if condition.

**3. Standard representation and core.** Assume \(W\) is PAV-optimal. Every type-\(A\) voter already obtains every approved candidate, and every type-\(A\cup C\) voter also obtains every approved candidate. A coalition that makes every member strictly better off must therefore comprise only type-\(A\cup\{b\}\) voters. To improve even one such voter's current utility \(r\), the coalition must purchase all \(r+1\) candidates in \(A\cup\{b\}\). However,
\[
q\ge\frac{pk}{r+1},\qquad n=p+h+q>q
\quad\Longrightarrow\quad
\frac{pk}{n}<r+1.
\]
Even the full set of these \(p\) voters cannot afford that deviation, proving core membership. Also, the only absent candidate \(b\) has \(p<(r+1)n/k\) supporters, each already approving \(r\) winners. Thus no group violates ordinary EJR+: levels up to \(r\) are met, and levels at least \(r+1\) have insufficient supporting voters.

**4. Sharp three-bloc threshold.** Suppose \(W\) is PAV-optimal but fails strong EJR+ up to one. Put \(t=(p+h)/p>1\) and \(z=q/p>0\). The two conditions in the theorem imply
\[
\frac{k}{r+1}\le z\le\frac{kt}{t+r}-t
=k+r-(t+r)-\frac{kr}{t+r}
\le k+r-2\sqrt{kr}=(\sqrt{k}-\sqrt r)^2.
\]
The last inequality is AM–GM. Since \(k>r\), this forces
\[
k\ge F(r):=\frac{r}{(1-1/\sqrt{r+1})^2}.
\]
Here \(F(1)=6+4\sqrt2>11\) and \(F(2)=6+3\sqrt3>11\). For \(r\ge3\), write \(u=\sqrt{r+1}\ge2\); then \(F(r)=u^2(u+1)/(u-1)\), whose derivative \(2u+2-2/(u-1)^2\) is positive on \([2,\infty)\). Consequently \(F(r)\ge F(3)=12\). In every case, integer \(k\) must be at least \(12\).

Conversely, for any integer \(k\ge12\), choose the parameters in the theorem. Then \(q/k=2+1/k>2=p/(r+1)\), giving a unique PAV winner. The largest payment in the coalition consisting of all \(p+h=16\) voters outside the \(A\cup C\) type equals
\[
\frac{2}{16}+\frac16=\frac7{24}
<\frac{k}{2k+17},
\]
where the strict inequality is equivalent to \(10k>119\), valid for all integer \(k\ge12\). Hence the unique PAV winner fails strong EJR+ up to one. At \(k=12\), the shortfall is \(12/41-7/24=1/984\), as claimed. This completes the proof.

## Verification

The included standalone `check_family.py` uses exact rational arithmetic. It computes PAV scores for every size-\(k\) committee directly from the approval ballots, independently evaluates the strong-EJR+ payment expression for every coalition-type count vector, and compares the outputs against the two claimed closed-form criteria. Its checks comprise \(810\) small-parameter families, \(55\) exact rational tests of the below-twelve necessary inequality, and \(13\) larger-family witnesses covering committee sizes \(12\) through \(24\). For the \(41\)-voter witness, it evaluates all \(1716\) relevant coalition-type vectors, which represent every distinct coalition approval signature, and verifies the unique PAV winner and the exact \(1/984\) gap. Run `python3 check_family.py` in the directory containing this report.

These computations are cross-checks. The unrestricted exact parameter classification and all-size threshold follow from the displayed analytical proof, not from a finite search.

## Relationship to prior work

Skowron (2026) introduced payment-based weak and strong variants of EJR+ for additive utilities. His Section 3.3 establishes that strong EJR+ up to one can reject core-stable and ordinary-EJR+ outcomes. Section 5 relates standard PAV optimization to the **weak** axiom. The inspected paper does not give the present PAV-optimality-versus-strong-EJR+ separation, the three-bloc if-and-only-if classification, or its sharp within-family seat threshold. The existing fact that PAV satisfies ordinary EJR+ does not imply strong EJR+ satisfaction, as demonstrated here. The source's original core-versus-strong counterexample is credited rather than claimed as a new discovery.

## Limitations

The twelve-seat minimality concerns only the explicitly specified three-bloc candidate-and-ballot template, not arbitrary approval elections. The result does not establish a universal minimum committee size for a PAV-versus-strong-EJR+ separation. The strong axiom is the payment-based *up-to-one* variant, not another similarly named proportionality criterion. The conclusion is a mathematical self-review, not independent validation. Earlier unindexed equivalent results remain a possible priority risk.

## References

- Piotr Skowron, *Robust Proportionality Axioms for Additive Utilities*, arXiv:2610.15516, first posted October 11, 2026, https://arxiv.org/abs/2610.15516. Relevant sections: 2 (PAV), 3.1–3.3 (EJR+ variants), 5 (PAV connection).
- Markus Brill and Jannik Peters, prior work introducing EJR+ and its relation to PAV, as cited and discussed in Skowron (2026), Sections 1 and 3. No unverified publication date is asserted here.
