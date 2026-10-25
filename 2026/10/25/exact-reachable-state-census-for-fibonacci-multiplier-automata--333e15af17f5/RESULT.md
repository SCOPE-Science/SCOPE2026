# Exact reachable-state census for Fibonacci multiplier automata

## Finding

For every integer \(m\ge1\) and every offset \(0\le c<m\), consider the standard bounded-difference automaton for the relation \(Y=mX+c\) between two *parallel*, most-significant-digit-first Zeckendorf representations. Its non-sink reachable-state count is exactly
\[
\boxed{|R_m|=6m^2+6m-4.}
\]
The reachable states, unlike the formal ambient state set, are independent of \(c\). More precisely, when the current difference coordinate is \(d\in\{-m,\ldots,2m-1\}\), the exact number is
\[
\boxed{r_m(d)=2m+2-\mathbf 1_{d=m-2}-\mathbf 1_{d=m-1}-\mathbf 1_{d=2m-2}-\mathbf 1_{d=2m-1}.}
\]
Indicators are counted with multiplicity when indices coincide (which matters for \(m=1\)). Deleting unreachable states therefore gives a recognizing automaton with precisely \(6m^2+6m-4\) non-sink states, improving the explicit \(36m^2\)-state ambient construction. This is **not** a claim about the minimum number of states of the language: subsequent DFA minimization can merge additional states.

## Assumptions and scope

Set \(F_2=1\), \(F_3=2\), and \(F_{i+2}=F_{i+1}+F_i\). A valid representation \(u=u_t\cdots u_2\) has digits in \(\{0,1\}\), contains no adjacent ones, and has value \([u]=\sum_{i=2}^t u_i F_i\). Arbitrary leading zeros are allowed. A pair \((u,v)\) is read synchronously with the same number of digits, using leading-zero padding where necessary.

Let \(I_m=\{-m,\ldots,2m-1\}\). A non-sink state is a quadruple \((a,b,d,e)\), where \(a,b\) are the last digits of the two prefixes, \(d=[v]-m[u]\), and \(e\) is the analogous difference one digit earlier. The initial state is \((0,0,0,0)\). From \((a,b,d,e)\), input \((s,t)\in\{0,1\}^2\) gives
\[
 (a,b,d,e)\longmapsto(s,t,d+e+b-ma+t-ms,d)
\]
provided \(as\ne1\), \(bt\ne1\), and the new difference belongs to \(I_m\); otherwise the transition is undefined (or goes to a rejecting sink). States with \(d=c\) are accepting. Only reachable states that have not entered the sink are counted, including those that might later fail to reach an accepting state.

## Proof

**1. Zeckendorf shift and last-digit formulae.** Put \(\phi=(1+\sqrt5)/2\), \(\theta=1/\phi\), and \(g(z)=\lfloor(z+2)\theta\rfloor-1\). For every valid finite representation of \(z\), deleting the final digit gives the valid representation of \(g(z)\). Here is a direct justification. For any valid prefix \(x\), the Fibonacci recurrence and Binet identity yield
\[
 \epsilon_x=[x0]-\phi[x]=\sum_{i\ge2}x_i(-\theta)^i,
 \qquad -\theta^2<\epsilon_x<\theta.
\]
The bounds follow by summing the negative odd and positive even geometric series; they are strict for finite strings. If \(x\) ends in zero, its positive even terms start no earlier than index four, giving the sharper bound \(\epsilon_x<\theta^3\). Writing \(z=[xa]=\phi[x]+\epsilon_x+a\) for \(a\in\{0,1\}\), with \(x\) ending in zero whenever \(a=1\), gives \(\phi<2+\epsilon_x+a<2\phi\). Therefore \(g(z)=[x]\).

For \(z\ge0\) put \(\delta_z=\{(z+2)\theta\}\), where braces denote fractional part. The displayed formula for \(g\) gives
\[
 z-\phi g(z)=\phi\delta_z-\theta^2.
\]
If the last Zeckendorf digit of \(z\) is \(a\), the left side also equals \(\epsilon_x+a\). The preceding strict bounds imply the sharp threshold
\[
 a=0\ \Longleftrightarrow\ \delta_z<\theta,
 \qquad a=1\ \Longleftrightarrow\ \delta_z>\theta.
\]
Equality never occurs for nonnegative integer \(z\), by irrationality of \(\theta\).

**2. No hidden state loss from the difference window.** For any two nonnegative values \(X,Y\), set \(d=Y-mX\), \(\delta=\delta_X\), and \(\beta=(d+2-2m)\theta\). Then the difference one digit earlier equals
\[
 e=g(Y)-mg(X)=\lfloor m\delta+\beta\rfloor+m-1. \tag{1}
\]
If \(-m\le d\le2m-1\), then \(e\in I_m\): since \(0<\delta<1\),
\[
 m\delta+\beta>(-3m+2)\theta>-2m+1,
 \qquad m\delta+\beta<m+\theta.
\]
Both inequalities imply \(-m\le e\le2m-1\). Repeatedly removing the last digit proves **backward closure** of \(I_m\). Thus every padded valid pair whose *final* difference is in \(I_m\) follows a completely non-sink path; the interval restriction excludes none of the states described by (1). Conversely, every reachable state is obtained from some such pair.

**3. Exact state count at each fixed difference.** Fix \(d\in I_m\), choose any large \(X\ge0\), and put \(Y=mX+d\ge0\). The fractional parts \(\delta=\{(X+2)\theta\}\) are dense in \((0,1)\) as \(X\) ranges through positive integers. By Step 1, the last input bits and the preceding difference of the resulting state are precisely
\[
 a=\mathbf1_{\delta>\theta},\qquad
 b=\mathbf1_{\{m\delta+\beta\}>\theta},\qquad
 e=\lfloor m\delta+\beta\rfloor+m-1.
\]
For fixed \(d\), this triple is constant on each open interval between the breakpoints
\[
 \delta=\theta,\qquad
 m\delta+\beta\in\mathbb Z,\qquad
 m\delta+\beta\in\mathbb Z+\theta.
\]
Different intervals give different triples: the value of \(e\) increases at integer crossings, \(b\) changes at \(\mathbb Z+\theta\) crossings, and \(a\) changes at \(\delta=\theta\). Every interval is visited by infinitely many \(X\), and the backward-closure argument makes its state reachable.

Over an interval of \(\delta\)-length one, each of the two lattice families normally contributes exactly \(m\) interior crossings. The \(\mathbb Z\) family contributes only \(m-1\) when \(\beta\in\mathbb Z\), which by irrationality happens precisely when \(d=2m-2\); the \(\mathbb Z+\theta\) family similarly loses one when \(d=2m-1\). The additional crossing \(\delta=\theta\) coincides with a lattice crossing precisely when
\[
 m\theta+\beta=(d+2-m)\theta\in\mathbb Z\cup(\mathbb Z+\theta),
\]
that is, precisely for \(d=m-2\) or \(d=m-1\), respectively. Thus the number of distinct intervals and states is the stated \(r_m(d)\). Summing over the \(3m\) admissible values of \(d\), and observing that each of the four exceptional indicators contributes once, gives
\[
 |R_m|=3m(2m+2)-4=6m^2+6m-4.
\]
This proves the theorem for all integers \(m\ge1\), including the overlapping exceptional indices when \(m=1\).

**4. Recognition consequence.** The transition recurrence tracks \(d=[v]-m[u]\) exactly by \([x00]=[x]+[x0]\). A difference below \(-m\) stays below \(-m\) under every valid right extension by the preceding shift-error bounds. A difference at least \(2m\) produces a next difference at least \(m\), after which two consecutive differences at least \(m\) force every later difference to stay at least \(m\): at most one of two consecutive input digits in the first track is one, so the two-step recurrence can subtract at most \(m\). Therefore no rejected out-of-window prefix can be extended to a word with final difference \(c\in\{0,\ldots,m-1\}\). The reachable-state restriction still recognizes exactly \([v]=m[u]+c\) on valid padded representations.

## Verification

The standalone script `verify_reachable.py` constructs the transition graph with exact integer arithmetic and independently counts the predicted circle cells. It confirms the formula and the complete per-difference profile for every \(m\) from 1 through 60. For \(m\le12\), a separate enumeration of actual Zeckendorf numeral pairs with source values 0 through 2999 reproduces the entire reachable-state set without using the transition recurrence. Running `python verify_reachable.py` produces the attached `verification_output.json`. The infinite formula is established by the proof, not by this finite test.

## Relationship to prior work

Moradi, Rampersad, and Shallit, *Complexity of Linear Subsequences of Fibonacci-Automatic Sequences* (arXiv:2603.21645v1, 23 March 2026), Section 3.2, construct the same bounded-difference four-coordinate automaton and give the ambient count \(36m^2\) as an \(O(m^2)\) bound. Their Remark 12 specifically discusses further state minimization and gives selected exact minimal-DFA counts. The present result computes instead the exact **reachable, unminimized** part and its complete current-difference profile, which is not supplied by that ambient bound. The two counts are not interchangeable.

Charlier, Rampersad, Rigo, and Waxweiler, *State Complexity of Testing Divisibility* (arXiv:1008.1668v1, 2010), determine \(2m^2\) as the number of trim minimal states of a **single-track divisibility language**. Their one-input result does not count states of this two-track multiplier-relation construction. The related base-\(k\) treatment in Moradi, Rampersad, and Shallit (arXiv:2512.10017) works in a different positional numeration system. OEIS A372846 tabulates *minimal* two-track counts for offset zero, a different invariant.

## Limitations

The theorem concerns one specified difference-window automaton, its exact reachable states before minimization, and valid Zeckendorf representations with arbitrarily padded leading zeros. It does not determine the Myhill–Nerode state complexity of the multiplier relation. In particular, \(6m^2+6m-4\) is a constructive upper bound for the non-sink DFA size, **not** an exact language minimum or a lower bound. Other automaton constructions may be smaller. Delaram Moradi's 2026 thesis, *State Complexity of Linear Relations and Linear Subsequences of Automatic Sequences*, was inspected in full in its relevant chapter (Chapter 3, especially pp. 54–57). It reproduces the ambient \(36m^2\) bound and, in Remark 46, calls for a better understanding of reachable states; it does not supply the formula proved here. Unindexed equivalent work remains a historical-priority risk.

## References

1. D. Moradi, N. Rampersad, J. Shallit, *Complexity of Linear Subsequences of Fibonacci-Automatic Sequences*, arXiv:2603.21645v1 (2026), especially Section 3.2 and Remark 12. https://arxiv.org/html/2603.21645v1
2. É. Charlier, N. Rampersad, M. Rigo, L. Waxweiler, *State Complexity of Testing Divisibility*, arXiv:1008.1668v1 (2010), Sections 1–3. https://arxiv.org/html/1008.1668v1
3. D. Moradi, N. Rampersad, J. Shallit, *Complexity of Linear Subsequences of \(k\)-Automatic Sequences*, arXiv:2512.10017v5 (2026), Sections 1 and 3. https://arxiv.org/html/2512.10017v5
4. D. Moradi, *State Complexity of Linear Relations and Linear Subsequences of Automatic Sequences*, Master of Mathematics thesis, University of Waterloo (2026), Chapter 3, especially Theorem 41 and Remark 46. https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/01edd675-7b51-46c3-b9b5-5a90c01a59b6/content
5. OEIS A372846, minimal state count for two-track multiplication in Zeckendorf numeration. https://oeis.org/A372846
