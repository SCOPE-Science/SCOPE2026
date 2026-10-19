# Exact variance profile of random-input pair synchronization in Černý automata

## Finding

For every integer \(n\ge3\), consider the deterministic two-letter automaton with state set \(Q=\{0,1,\ldots,n-1\}\), rotation \(a(t)=t+1\pmod n\), and merge letter \(b(n-1)=0\), \(b(t)=t\) for \(0\le t<n-1\). Feed independent fair letters \(a,b\). For distinct initial states \(0\le i<j<n\), let \(T_{i,j}\) be the number of letters until both images first agree, and put \(d=j-i\). Define

\[
A_n=4n^5-10n^4+8n^3+n^2-7n+2,
\qquad B_n=24n^4-48n^3+32n^2-2n-7.
\]

Then the **exact variance for every initial pair** is

\[
\boxed{\operatorname{Var}(T_{i,j})=
\frac{4d A_n-2d^2 B_n+8d^3(2n-1)^3-8d^4(2n-1)^2}{3}-2i.}
\]

For comparison, its exact mean is

\[
\mathbb E T_{i,j}=4dn(n-d-1)+2d^2-2i.
\]

The pair attaining the largest mean is uniquely \(\{0,\lfloor n/2\rfloor\}\). For that pair,

\[
\mathbb E T_{0,\lfloor n/2\rfloor}\sim n^3,
\qquad \operatorname{Var}(T_{0,\lfloor n/2\rfloor})\sim\frac23n^6,
\]

and consequently

\[
\boxed{\lim_{n\to\infty}\frac{\sqrt{\operatorname{Var}(T_{0,\lfloor n/2\rfloor})}}{\mathbb E T_{0,\lfloor n/2\rfloor}}=\sqrt{2/3}.}
\]

Thus random-letter pair recovery at the slowest-mean starting pair has a nonvanishing relative standard deviation.

## Assumptions and scope

The word of incoming letters is independent and identically distributed with \(\Pr(a)=\Pr(b)=1/2\), and its action on both states is simultaneous. The random time counts the merging letter itself. The initial pair is unordered, represented with \(i<j\). All claims hold for every integer \(n\ge3\) and every distinct initial pair. This is a **pair-coalescence** theorem, not a claim about the first time the *entire* state set is synchronized. Only the uniform-letter case is asserted; no independence of different initial-pair stopping times is assumed.

## Proof

**1. Finiteness and first-moment boundary equations.** A fixed reset word for this automaton is \(b(a^{n-1}b)^{n-2}\). It appears with positive probability within each independent block of its length, so every pair-coalescence time is bounded above by a geometric number of blocks and has all moments finite. The resulting finite-state moment equations have unique finite solutions.

Put \(F_0=0\) and \(F_d=\mathbb E T_{0,d}\) for \(1\le d<n\). For a current pair \(\{r,r+d\}\) with \(r+d<n-1\), letter \(b\) fixes the pair; letter \(a\) advances both positions. First-step conditioning gives \(\mathbb ET_{r,r+d}-\mathbb ET_{r+1,r+d+1}=2\). At \(r=L=n-1-d\), a rotation sends the pair to \(\{0,L+1\}\), while the merge sends it to \(\{0,L\}\), where \(L=0\) means immediate coalescence. Therefore

\[
F_d=2L+1+\frac{F_{L+1}+F_L}{2},\qquad L=n-1-d.
\]

Direct substitution gives the unique solution

\[
F_d=4dn(n-d-1)+2d^2,
\]

and advancing the initial pair \(i\) times gives the displayed formula for \(\mathbb E T_{i,j}\).

**2. Exact conditional-variance recursion.** For any nonabsorbing state \(s\), let \(s_a,s_b\) denote the states after the two letters. The law of total variance, together with the first-step decomposition of \(T\), gives

\[
V_s=\frac{V_{s_a}+V_{s_b}}2
+\frac{(E_{s_a}-E_{s_b})^2}{4},
\]

where \(E_s=\mathbb ET_s\), \(V_s=\operatorname{Var}(T_s)\), and both moments vanish at the absorbed state. Where the merge letter fixes the current pair, the two successor means differ by \(2\), and hence \(V_{r,r+d}-V_{r+1,r+d+1}=2\). Set \(G_0=0\), \(G_d=V_{0,d}\). At the first pair containing \(n-1\), the successor means are \(F_{L+1}\) and \(F_L\), so

\[
G_d=2L+\frac{G_{L+1}+G_L}{2}
+\frac{(F_{L+1}-F_L)^2}{4},\qquad L=n-1-d.
\]

**3. Solving the variance boundary equations.** Define

\[
G_d=\frac{4d A_n-2d^2 B_n+8d^3(2n-1)^3-8d^4(2n-1)^2}{3}.
\]

Expanding the polynomials in the previous identity verifies it for every \(n,d\), with \(G_0=0\). Because pair absorption is almost sure with finite second moment, this is the unique finite solution of the variance equations. The nonboundary relation gives \(V_{i,j}=G_{j-i}-2i\) for all \(i<j\). No finite enumeration is used to infer this arbitrary-size identity.

**4. Worst-mean pair and nonconcentration.** For \(d=j-i\), the mean is \(F_d-2i\), so at each gap it is largest at \(i=0\). The quadratic \(F_d=-(4n-2)d^2+4n(n-1)d\) has its unique integer maximum at \(d=\lfloor n/2\rfloor\). Substitution of \(d=\lfloor n/2\rfloor\) into \(F_d\) and \(G_d\), separately for odd and even \(n\), yields the leading terms \(n^3\) and \((2/3)n^6\), proving the stated limit.

## Verification

The standalone file `verify.py` uses only the Python standard library. Run `python3 verify.py`. It independently solves the raw transient pair-state Markov matrices over exact rational numbers, with no use of the closed formulas in constructing those matrices, for every initial pair at \(3\le n\le8\). It checks mean and variance against the formulas. It also evaluates the two displayed polynomial boundary identities on an \(8\times8\) rectangular grid. Both residuals are bivariate polynomials whose degree in either variable is at most six, so the zero-grid check itself supplies an algebraic identity certificate once the degree bound is established. Expected output:

`VERIFY_OK polynomial_grid_8x8 exact_pair_markov_moments n=3..8 states=83`

The infinite claim is proved by the recurrence and its polynomial identity, not by finite Markov-matrix evaluation.

## Relationship to prior work

Gusev (2014), arXiv:1404.6731, studies the same independent random-input process on the Černý automata and establishes exact **expected** pair-coalescence times for worst starting pairs. His Section 3, Theorems 3–4 and equations (14)–(20), analyze first moments, not the complete second-moment or variance profile or the limiting relative standard deviation. Accordingly, the displayed mean formula is background and is **not claimed as new**. The present theorem evaluates the second moments for every starting pair. The general Markov-chain variance identity alone supplies a finite linear system, not the explicit all-size quartic solution.

Kisielewicz, Kowalski and Szykuła (online 2013) study algorithms and experimental distributions for **shortest reset words of sampled automata**. Their random variable is not the time to synchronize a fixed Černý pair under random input. That distinction is essential when comparing variance statements.

## Limitations

The assertion concerns uniformly random letters; biased-letter variance polynomials are not established here. Coalescence of a pair is not synchronization of all states. The result is exact but lacks independent scientific audit. Possible earlier or differently indexed variance formulas could affect priority; the accessible comparisons below are not a uniqueness certificate. No claim of concentration or a full limiting distribution is made.

## References

1. V. V. Gusev, *Synchronizing Automata with Random Inputs*, arXiv:1404.6731v1 (first public April 27, 2014), especially Section 3. https://arxiv.org/pdf/1404.6731
2. A. Kisielewicz, J. Kowalski, M. Szykuła, *Computing the Shortest Reset Words of Synchronizing Automata*, *Journal of Combinatorial Optimization* 29 (2015), 88–124; first published online November 17, 2013. DOI: 10.1007/s10878-013-9682-0.
