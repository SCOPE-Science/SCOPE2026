# A reverse-index iterated-logarithm hierarchy for iterated harmonic numbers

## Finding
For integers \(j\ge1\) and \(n\ge1\), define
\[
h_1(n)=\sum_{k=1}^{n}\frac1k,\qquad h_j(n)=\sum_{k=1}^{n}\frac{1}{k\prod_{i=1}^{j-1}h_i(k)}\quad(j\ge2),
\]
and \(P_j(n)=\prod_{i=1}^j h_i(n)\), with \(P_0(n)=1\). Write \(\log_1 t=\log t\), \(\log_{r+1}t=\log(\log_rt)\) on their eventual positive domains, and interpret an empty product as 1. Then, for **every fixed integer** \(n\ge2\), as \(j\to\infty\),
\[
\boxed{P_j(n)\sim\frac jn\prod_{r=1}^{n-2}\log_r j.}
\]
Moreover, for every fixed \(n\ge3\),
\[
\boxed{\lim_{j\to\infty}j\log j\left(h_j(n)-1-\frac1{j+1}\right)=1,}
\]
whereas \(h_j(2)=1+1/(j+1)\) exactly. In particular, for every fixed \(n\ge2\), \(j(h_j(n)-1)\to1\).

## Assumptions and scope
All \(h_j(n)\) are positive rational numbers defined by the displayed finite nested sums. The asymptotic variable is the iteration index \(j\), **not** the summation endpoint \(n\), and \(n\) is fixed. For each finite \(n\), every sufficiently large \(j\) makes the iterated logarithms defined and positive. The notation \(f_j\sim g_j\) means \(f_j/g_j\to1\). No uniformity is asserted when \(n\) grows with \(j\). The result says nothing about nonintegrality at fixed iteration depth for all endpoints.

## Proof
**1. An exact transposed recurrence.** The defining sums give \(h_j(n)-h_j(n-1)=1/(nP_{j-1}(n))\) for \(n\ge2\). Put \(Q_j(n)=P_j(n)/P_j(n-1)\), with \(Q_0(n)=1\). Since \(P_j=P_{j-1}h_j\), exact cancellation yields
\[
Q_j(n)-Q_{j-1}(n)=\frac{1}{nP_j(n-1)}.
\]
Indeed the difference equals \(Q_{j-1}(n)(h_j(n)-h_j(n-1))/h_j(n-1)\), and substituting the sum increment gives the right side. Hence, setting \(T_j(n)=\sum_{i=1}^j1/P_i(n)\),
\[
\boxed{Q_j(n)=1+\frac{T_j(n-1)}n.}\tag{1}
\]
Also \(P_j(1)=1\) for every \(j\). At \(n=2\), direct summation/telescoping gives \(h_j(2)=(j+2)/(j+1)\), \(P_j(2)=(j+2)/2\).

**2. Induction along the endpoint.** For an integer \(n\ge2\), let \(L_n(t)=\prod_{r=1}^{n-2}\log_r t\) (thus \(L_2(t)=1\)). We prove
\[
P_j(n)\sim \frac{jL_n(j)}n.\tag{2}
\]
The base \(n=2\) is the exact expression above. Suppose (2) is established at \(n-1\ge2\). Then
\[
\frac1{P_j(n-1)}\sim\frac{n-1}{jL_{n-1}(j)}.
\]
By the integral test and the exact derivative \(d(\log_{n-2}t)/dt=1/(tL_{n-1}(t))\),
\[
T_j(n-1)=\sum_{i=1}^j\frac1{P_i(n-1)}\sim(n-1)\log_{n-2}j.\tag{3}
\]
The initial finite indices where an iterated logarithm is not defined affect no asymptotic. To justify summing the asymptotic, sandwich its tail between \((1\pm\varepsilon)(n-1)/(iL_{n-1}(i))\) and note that the comparison series diverges. From (1) and (3),
\[
Q_j(n)\sim\frac{n-1}{n}\log_{n-2}j.
\]
Multiplying by the induction hypothesis for \(P_j(n-1)\) proves (2). No unproved interchange of limits is used: this induction is separately valid for each fixed integer \(n\).

**3. The leading two terms of each iterate.** For every \(j\ge1\), split the defining finite sum at the first two endpoints:
\[
h_j(n)-1=\frac1{j+1}+\sum_{k=3}^n\frac1{kP_{j-1}(k)}\qquad(n\ge2),\tag{4}
\]
where the sum is empty for \(n=2\). Formula (2) at \(k=3\) gives \(P_{j-1}(3)\sim(j/3)\log j\), so the \(k=3\) contribution is asymptotic to \(1/(j\log j)\). For each fixed \(k\ge4\), (2) gives
\[
\frac1{kP_{j-1}(k)}\sim\frac{1}{j\prod_{r=1}^{k-2}\log_r j}=o\!\left(\frac1{j\log j}\right).
\]
Since the remaining sum has finitely many terms for fixed \(n\), (4) proves the second boxed limit and the claimed first-order limit. \(\square\)

## Verification
The included `verify.py` independently constructs all finite sums using exact rational arithmetic for \(1\le j\le8\) and \(1\le n\le7\), verifies (1), verifies the exact \(n=2\) identities, and checks the finite positive-parameter recurrence. It is a regression test, not an infinite proof. Run `python3 verify.py`; the included `verification_output.txt` records one successful execution. The asymptotic proof is the algebra and fixed-index integral comparison above.

## Relationship to prior work
Ash, Ash, Ash and Plaza (arXiv:2303.02832, first publicly posted 2023-03-06; revised 2023-04-11) introduced these iterated harmonic numbers, studied **fixed iteration depth with endpoint tending to infinity**, and proposed an integrality conjecture. Section 7 explicitly raises monotonicity in the iteration index as a question. Here the asymptotic variable is instead iteration depth with endpoint fixed, and the exact transposed recurrence (1) yields a complete nested-logarithm product hierarchy. The later 2026 journal version has an added coauthor (McNew); its publicly accessible abstract retains the forward-index focus. No implication from the reported endpoint asymptotics yields this reverse-index theorem. This theorem does **not** settle the conjecture that \(h_j(n)\) is nonintegral for all \(j\ge2,n\ge2\).

## Limitations
The formulas require \(n\) fixed as \(j\to\infty\); no uniform statement is given as both indices vary. The second boxed limit proves only asymptotic nonintegrality for fixed \(n\), not all endpoints for a fixed \(j\). A potentially expanded 2026 final journal text was not fully accessible and remains a bibliographic comparison risk; the 2023 source was inspected materially in full through its lawful HTML edition. The sequence is a special rational number-theoretic sequence; the primary classification assigned here is 11B83.

## References
1. J. Marshall Ash, Michael Ash, Rafael Ash, and Ángel Plaza, *Iterated harmonic numbers*, arXiv:2303.02832v2 (2023), https://arxiv.org/html/2303.02832v2 (original public posting March 6, 2023).
2. J. Marshall Ash, Michael Ash, Rafael Ash, Nathan McNew, and Ángel Plaza, *Iterated Harmonic Numbers*, College Mathematics Journal 57 (2026), 193–205, doi:10.1080/07468342.2026.2621673 (later version of the same work).
