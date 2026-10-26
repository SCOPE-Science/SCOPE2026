# Exact Gaussian-cone law at the two-seat AJR critical point

## Finding
Let there be three named candidates and \(n\) voters. Each voter independently approves each candidate with probability \(1/2\). For each committee \(W\) of size two, average justified representation (AJR) requires that every group of at least \(\ell n/2\) voters sharing at least \(\ell\) approved candidates have average utility at least \(\ell\), for \(\ell\in\{1,2\}\); voter utility is the number of candidates they approve in \(W\). Let \(P_n\) be the probability at least one committee has AJR.

Set \(I=I_3\) and \(J=\mathbf 1\mathbf 1^{\mathsf T}\), and define
\[
\Sigma=\frac18\begin{pmatrix}2I&3I-J\\3I-J&5I-J\end{pmatrix}.
\]
For a centered six-variate normal vector \(G\) with covariance \(\Sigma\),
\[
\lim_{n\to\infty}P_n=1-\Pr(G_1>0,\ldots,G_6>0).
\]
The six-dimensional orthant integral gives a numerical value approximately \(0.9840\), without an independently certified decimal interval. Every fixed two-seat committee has asymptotic AJR probability exactly \(5/8\), so the expected number of AJR committees tends to \(15/8\). This is an exact limiting distributional characterization at the critical approval probability, not an asymptotic existence-versus-nonexistence dichotomy.

## Assumptions and scope
The number of candidates is exactly three and the committee has exactly two seats. All \(3n\) approval bits are independent Bernoulli variables of parameter \(1/2\); \(n\) tends through all positive integers. Write \(B_{ic}\in\{0,1\}\) for voter \(i\)'s approval of candidate \(c\in\{1,2,3\}\). The quota is \(q=\lceil n/2\rceil\). Whenever \(c\) is excluded from the committee, denote the other candidates by \(a,b\), and let
\[
N_c=\sum_{i=1}^{n}B_{ic},\qquad L_c=\sum_{i=1}^{n}B_{ic}(2-B_{ia}-B_{ib}).
\]
The statistics \(N_c\) and \(L_c\) are respectively the number of \(c\)-supporters and their total deficit from the maximum committee utility two. For a fixed \(c\), let \(N_{c,j}\) count its supporters with exactly \(j\) approvals among the two committee members, for \(j=0,1,2\); then \(L_c=2N_{c,0}+N_{c,1}\).

## Proof
**Reduction of coalition tests.** A one-cohesive group sharing any selected candidate has every member's committee utility at least one, hence cannot violate AJR. Consequently, the only one-cohesive obstruction for the committee excluding \(c\) comes from a subgroup of at least \(q\) supporters of \(c\). Their lowest possible average utility occurs among the \(q\) supporters with smallest utilities: for any longer group, the ordered-prefix average cannot decrease. If \(N_c<q\), this obstruction is absent.

Let \(H_c=N_{c,0}+N_{c,1}\). On the event \(H_c<q\), if \(N_c\ge q\), the worst \(q\)-member group contains all \(N_{c,0}\) zero-utility supporters, all \(N_{c,1}\) one-utility supporters, and \(q-H_c\) two-utility supporters. Its sum of utilities is \(2q-2N_{c,0}-N_{c,1}=2q-L_c\). Therefore this excluded-candidate committee fails the one-cohesive AJR condition **if and only if** \(N_c\ge q\) and \(L_c>q\), provided \(H_c<q\).

For each voter, the event of approving \(c\) and approving at most one of the other two has probability \(3/8\). Thus \(H_c\sim\mathrm{Bin}(n,3/8)\) and Hoeffding's inequality gives \(\Pr(H_c\ge q)\le e^{-n/32}\). A two-cohesive group must contain at least \(n\) voters, hence must consist of all voters and all must approve at least one common pair of candidates. The probability of this exceptional event is at most \(3\cdot4^{-n}\). Therefore, except on an event of probability at most \(3e^{-n/32}+3\cdot4^{-n}\), **all three** committees fail AJR exactly when \(N_c\ge q\) and \(L_c>q\) for each \(c=1,2,3\).

**Multivariate limit.** For a single voter define the centered vector
\[
Z=(B_1-\tfrac12,B_2-\tfrac12,B_3-\tfrac12,\ B_1(2-B_2-B_3)-\tfrac12,\ B_2(2-B_1-B_3)-\tfrac12,\ B_3(2-B_1-B_2)-\tfrac12).
\]
Direct averaging over the eight equiprobable approval ballots gives \(\mathbb EZ=0\) and \(\mathbb E[ZZ^{\mathsf T}]=\Sigma\) above; \(\det\Sigma=2^{-16}\), so the Gaussian law is nondegenerate. The multivariate central limit theorem gives
\[
n^{-1/2}(N_1-n/2,N_2-n/2,N_3-n/2,L_1-n/2,L_2-n/2,L_3-n/2)\Longrightarrow G.
\]
Because \(q-n/2\) is bounded and Gaussian coordinate hyperplanes have probability zero, the probability of all six inequalities \(N_c\ge q,L_c>q\) converges to \(\Pr(G_1>0,\ldots,G_6>0)\). The exponentially unlikely exceptional events do not change the limit. Positive definiteness ensures that this orthant event and its complement both have positive probability.

**Fixed-committee limit.** For one candidate \(c\), the asymptotic event of failure has two centered normal coordinates \(N_c,L_c\), with variances \(1/4\) and \(1/2\) and covariance \(1/4\); their correlation is \(1/\sqrt2\). The centered bivariate normal quadrant formula yields
\[
\Pr(G_{N_c}>0,G_{L_c}>0)=\frac14+\frac{\arcsin(1/\sqrt2)}{2\pi}=\frac38.
\]
The fixed-committee AJR success probability tends to \(1-3/8=5/8\). Summing over the three committees proves the expected-number limit \(3(5/8)=15/8\).

## Verification
The accompanying standalone Python program, `checks/check_ajr_boundary.py`, enumerates the eight voter ballots with rational arithmetic to reconstruct all \(36\) covariance entries, checks the bivariate covariance and exact fixed-committee limit, and exhaustively compares the reduced feasibility event against the original coalition definition outside the explicitly identified exceptional events for every labelled approval profile with \(n\in\{2,3,4\}\). The program does not prove a central limit theorem or numerically certify the six-dimensional Gaussian integral; those components are established analytically or left as approximations, respectively. Run from the containing directory with `python checks/check_ajr_boundary.py` (Python standard library only).

## Relationship to prior work
Han, Tao, Xia, Zhang, and Zhou's 2025 preprint (later SODA 2026) proves the general phase diagram and, specifically for two seats at approval rate \(1/2\), proves that the probability of AJR committee existence and nonexistence are each bounded away from zero. Its Theorem 2.2 and phase-boundary analysis in Section 5 do not provide this explicit six-dimensional orthant probability or the exact fixed-committee probability. The present result refines that unresolved **quantitative** endpoint for the smallest three-candidate instance; it does not extend the general threshold characterization. Related work by Ai and Tao concerns computational decision complexity rather than the present limiting law; its publicly inspected abstract alone cannot exclude all related results.

## Limitations
The formula concerns only three candidates, two seats, independent uniform approvals, and the large-electorate limit. It does not supply a closed form for the six-dimensional orthant probability in elementary constants, a certified decimal interval, or quantitative convergence rates beyond the explicitly bounded exceptional-event reduction. Finite brute-force checks support algebraic identities but are not a proof for all electorate sizes. The literature comparison is not an exhaustive priority certificate; same-topic works not fully inspected remain possible. Independent audit has not been performed.

## References
1. Q. Han, B. Tao, L. Xia, C. Zhang, H. Zhou, *Likelihood of the Existence of Average Justified Representation*, arXiv:2510.18718, first public 2025-10-21, https://arxiv.org/abs/2510.18718; SODA 2026, DOI:10.1137/1.9781611978971.63.
2. Y. Ai and B. Tao, *Computational Complexity of Strong and Average Justified Representation*, arXiv:2606.29643, 2026, https://arxiv.org/abs/2606.29643 (abstract inspected for topic comparison).
