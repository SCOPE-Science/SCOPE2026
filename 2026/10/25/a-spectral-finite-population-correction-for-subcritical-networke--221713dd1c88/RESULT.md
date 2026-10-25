# A spectral finite-population correction for subcritical networked SIR outbreaks

## Finding

Fix an integer \(n\ge1\), an \(n\times n\) symmetric, nonnegative, row-stochastic matrix \(P\), and a reproduction ratio \(0<R<1\). Each of \(n\) patches contains exactly \(M\) individuals. Initially exactly one individual is infected, uniformly over the \(nM\) individuals, and all others are susceptible. Let \(T_M\) count everyone infected during a Markovian susceptible–infected–removed (SIR) outbreak, **including the initial case**. As \(M\to\infty\), with \(n,P,R\) fixed,

\[
\mathbb E T_M = \frac1{1-R}-\frac{K(P,R)}M+o(M^{-1}),
\qquad
K(P,R)=\frac{R}{n(1-R)^2}\operatorname{tr}\!\left[P(I-RP)^{-2}\right].
\]

The coefficient is positive and has the closed-walk representation

\[
K(P,R)=\frac{1}{n(1-R)^2}\sum_{k=1}^{\infty}kR^k\operatorname{tr}(P^k)>0.
\]

For any symmetric nonnegative row-stochastic \(Q\ne I\), increasing within-patch mixing along \(P_\theta=\theta I+(1-\theta)Q\), \(0\le\theta\le1\), strictly increases \(K(P_\theta,R)\). Thus the leading subcritical branching mean does not reveal network topology, whereas its first finite-patch-size correction does, with a universal direction under this mixing intervention.

## Assumptions and scope

The population is partitioned into \(n\) labelled patches, each of size \(M\ge1\). An infected person in patch \(i\) generates potential transmissions to patch \(j\) at rate \(\beta P_{ij}\), independently of other people; a potential transmission chooses a uniformly random person among the \(M\) inhabitants of patch \(j\), infecting the target if and only if still susceptible. Each infectious person recovers independently at rate \(\gamma>0\), never again becoming susceptible. We use \(R=\beta/\gamma<1\) and rescale physical time by \(\gamma\), so recovery rate is one and potential birth rate is \(R P_{ij}\). The count process has transition rates

\[
(S_j,I_j)\longmapsto(S_j-1,I_j+1)
\quad\text{at rate}\quad
\frac R M S_j\sum_{i=1}^nP_{ij}I_i,
\]

and \(I_i\mapsto I_i-1\) at rate \(I_i\). Put \(C_i(t)=M-S_i(t)\), the cumulative infected count, including all recoveries. The claim concerns the exact continuous-time stochastic model, not deterministic final-size equations, and does not assume \(P\) is irreducible or that its diagonal is positive. Symmetry and stochasticity are essential for the displayed trace formula and monotonicity statement. Parameters and the number of patches are held fixed as the population per patch grows.

## Proof

**1. Exact finite-population census.** Let \(A_M\) be the total number of successful infections beyond the seed. Integrate the total infection intensity and use the expected infectious lifetime \(1\) for every infected person: the expected total infectious person-time equals \(\mathbb E T_M\). Since every row of \(P\) sums to one and \(S_j=M-C_j\), the total infection intensity equals

\[
R\sum_i I_i(t)-\frac RM\sum_{i,j}P_{ij}I_i(t)C_j(t).
\]

Consequently, if

\[
J_M:=\mathbb E\int_0^\infty\sum_{i,j}P_{ij}I_i(t)C_j(t)\,dt,
\]

then

\[
(1-R)\mathbb E T_M=1-\frac RM J_M. \tag{1}
\]

Here all expectations are finite: the total birth intensity never exceeds \(R\sum_i I_i\) and hence the SIR epidemic is dominated by a subcritical birth–death branching process.

**2. Convergence to a multitype branching collision functional.** Construct a multitype branching process \(Z_i(t)\) with death rate one and independent births of type \(j\) from each type \(i\) at rate \(R P_{ij}\), starting from one uniformly selected type. Let \(B_i(t)\) count all type-\(i\) individuals born up to time \(t\), including the seed. Label each attempted type-\(j\) birth by a uniformly sampled person in patch \(j\), discarding that birth and all its descendants in the SIR process if the chosen person has already been infected. This couples the finite epidemic to the branching genealogy so that for every time and type, \(0\le I_i(t)\le Z_i(t)\) and \(0\le C_i(t)\le B_i(t)\).

The branching genealogy has finite total size almost surely and finite second moment: each person has a geometric number of children with mean \(R<1\), and the entire total progeny is subcritical. For a fixed realized finite genealogy, the probability that any of its finitely many independently chosen labels collide tends to zero as \(M\to\infty\). Thus the SIR states and their infection histories converge in the coupling to their branching counterparts on that realized genealogy. Because

\[
0\le\int_0^\infty\sum_{i,j}P_{ij}I_i C_j\,dt
\le\int_0^\infty \Bigl(\sum_i Z_i\Bigr)\Bigl(\sum_j B_j\Bigr)\,dt,
\]

and the expectation of the upper bound is finite (bound it by the squared branching total progeny times the maximal infectious lifetime, or by the moment equations below), dominated convergence implies

\[
J_M\longrightarrow J_\infty:=\mathbb E\int_0^\infty\sum_{i,j}P_{ij}Z_i(t)B_j(t)\,dt. \tag{2}
\]

For clarity, the upper bound can be justified without a maximal-lifetime shortcut: conditioning on the branching family size \(N\), each of its \(N\) lifetimes has mean one; total accumulated active lifetime weighted by the cumulative size is at most \(N\sum_{k=1}^N L_k\), and \(\mathbb E N^2<\infty\). The child count of an individual and its lifetime are correlated, so a safer direct bound is the finiteness of \(\mathbb E\int(\sum Z)(\sum B)dt\) obtained from the exact linear second-moment equations derived in step 3. The latter integrated-moment argument proves the dominating random variable integrable without any assumption of independent family size and lifetimes.

**3. Exact integrated branching moments.** Write column vectors \(Z,B\), set \(a=1-R\), \(D=I-RP\), and let \(\mathbf1\) be the all-ones column. Symmetry and stochasticity imply \(D\mathbf1=a\mathbf1\), and its eigenvalues lie in \([a,1+R]\), so \(D\) is invertible. The initial type is uniform, giving

\[
m(0)=\frac1n\mathbf1,\qquad
Y(0)=X(0)=\frac1n I,
\]

where \(m=\mathbb E Z\), \(Y=\mathbb E[ZZ^{\mathsf T}]\), and \(X=\mathbb E[ZB^{\mathsf T}]\). The Markov generator applied to linear and quadratic monomials gives, with \(\operatorname{diag}(v)\) denoting the diagonal matrix whose diagonal is \(v\),

\[
\begin{aligned}
m'&=-Dm,\\
Y'&=-DY-YD+\operatorname{diag}((I+RP)m),\\
X'&=-DX+RYP+R\operatorname{diag}(Pm).
\end{aligned}\tag{3}
\]

Each moment tends to zero as \(t\to\infty\): the generator equations have an exponentially stable homogeneous part and exponentially decaying forcing. The integrated mean is \(\bar m=\mathbf1/(na)\). Integrating the \(Y\) equation yields

\[
D\bar Y+\bar YD=\frac2{na}I,
\qquad\therefore\quad\bar Y=\frac1{na}D^{-1},
\]

where the Sylvester equation has a unique solution because \(D\) has strictly positive eigenvalues. Integrating the \(X\) equation then yields

\[
D\bar X=\frac1n I+\frac{R}{na}D^{-1}P+\frac{R}{na}I
=\frac1{na}D^{-1},
\qquad\therefore\quad\bar X=\frac1{na}D^{-2}. \tag{4}
\]

Therefore

\[
J_\infty=\sum_{i,j}P_{ij}\bar X_{ij}
=\frac1{na}\operatorname{tr}(PD^{-2}). \tag{5}
\]

Insert (2) and (5) into (1). Since \(R,a,n,P\) are fixed, the error is \(o(1/M)\), proving the main formula.

**4. Closed walks and strict monotonicity.** The convergent Neumann series \((I-RP)^{-2}=\sum_{k\ge0}(k+1)R^kP^k\) proves the stated walk expansion. Each \(\operatorname{tr}(P^k)\) is nonnegative because \(P\) has nonnegative entries, and at least one such trace is strictly positive: if all diagonal entries vanish, some off-diagonal positive edge exists by stochasticity and symmetry, hence \(\operatorname{tr}(P^2)>0\). Thus \(K>0\).

Let \(\mu_1,\ldots,\mu_n\in[-1,1]\) be the eigenvalues of \(Q\), with at least one \(\mu_i<1\) when \(Q\ne I\). The eigenvalues of \(P_\theta\) are \(\lambda_i(\theta)=\theta+(1-\theta)\mu_i\). For \(f_R(x)=x(1-Rx)^{-2}\),

\[
f_R'(x)=\frac{1+Rx}{(1-Rx)^3}>0
\qquad (-1\le x\le1,\;0<R<1).
\]

As \(\lambda_i(\theta)\) is nondecreasing, and some eigenvalue increases strictly, the sum \(K(P_\theta,R)=R[n(1-R)^2]^{-1}\sum_i f_R(\lambda_i(\theta))\) increases strictly as claimed.

## Verification

A standalone standard-library Python file, `verify.py`, reconstructs exact rational inverses of \(I-RP\), verifies the closed coefficient for three two-patch mixing levels, and independently evaluates finite-SIR expected total outbreak sizes by solving the exact finite-state recursion for small equal-size patches. It also checks an asymmetric-in-patch-index but symmetric-matrix three-patch case and the one-patch limit. Run `python verify.py` with no external dependencies. The analytic moment identities and coupling, not finite checks, establish the all-\(M\) asymptotic.

For \(R=1/2\), \(n=2\), and \(Q=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\), the exact coefficients at \(\theta=0,1/2,1\) are, respectively,

\[
K(P_0,1/2)=\frac{32}{9},\qquad K(P_{1/2},1/2)=4,\qquad K(P_1,1/2)=8.
\]

The one-patch specialization is \(K(1,R)=R/(1-R)^4\).

## Relationship to prior work

Ueki, Thompson, and Banaji (2026), especially their stochastic patch model, section 3.3 and supplementary branching approximations, motivate mean outbreak size and spatial architecture effects. Their examined results do not state this fixed-subcritical, first-inverse-patch-size spectral coefficient or its universal monotonicity along \(\theta I+(1-\theta)Q\). Wilkinson, Ball, and Sharkey (2017) give rigorous message-passing and stochastic-SIR bounds on finite graphs, not the displayed patch-size expansion. Bizzotto, Ball, and Britton (2026) give bounds for reproduction numbers and deterministic final epidemic size from partial next-generation matrices, not a correction to the stochastic minor-outbreak mean. The expansion uses established subcritical branching-process methods; neither the general coupling nor resolvent algebra is asserted to be independently novel. Searches and comparisons did not locate a theorem that implies the precise combined formula and monotonicity; this is a bounded literature assessment, not a proof of global priority.

## Limitations

The expansion holds only for fixed \(n\), fixed symmetric nonnegative stochastic \(P\), and fixed strictly subcritical \(R<1\) as \(M\to\infty\). It is not uniform as \(R\uparrow1\), and does not describe a critical or supercritical outbreak, unequal patch sizes, asynchronous movement, time-varying rates, additional latency compartments, or arbitrarily directed mixing. It gives the first correction but no claimed uniform finite-\(M\) error rate or exact ordering of \(\mathbb E T_M\) at every \(M\). Source priority, especially within general strong epidemic approximation theory, needs independent verification.

## References

1. M. Ueki, R. N. Thompson, M. Banaji, *Outbreak dynamics and population vulnerability in stochastic epidemic models on networks*, arXiv:2601.13730, first public January 20, 2026; relevant sections 2, 3.3, S1, S2. https://arxiv.org/html/2601.13730v2
2. R. R. Wilkinson, F. G. Ball, K. J. Sharkey, *The relationships between message passing, pairwise, Kermack–McKendrick and stochastic SIR epidemic models*, Journal of Mathematical Biology 75 (2017), 1563–1590. https://pmc.ncbi.nlm.nih.gov/articles/PMC5641366/
3. A. Bizzotto, F. Ball, T. Britton, *Bounds on R0 and final epidemic size when the next-generation matrix M is only partially known*, arXiv:2602.23885 (2026). https://arxiv.org/abs/2602.23885
4. F. Ball, P. Donnelly, *Strong approximations for epidemic models*, Stochastic Processes and their Applications 55 (1995), 1–21. General coupling background; only bibliographic record and abstract assessed.
