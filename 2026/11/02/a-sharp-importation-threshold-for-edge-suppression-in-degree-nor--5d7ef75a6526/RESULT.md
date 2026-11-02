# A sharp importation threshold for edge suppression in degree-normalized epidemic transmission

## Finding

Consider the continuous-time susceptible–infected–susceptible process with positive per-vertex spontaneous infection rate \(\alpha\), unit infected recovery rate, and total attempted transmission rate \(\beta\) **per infected source vertex**, which selects a uniform neighbor on each attempt. Let \(P_G(\alpha,\beta)\) be the stationary expected infected fraction on a finite connected simple undirected graph \(G\). Let \(C_4\) be the four-cycle and \(D=C_4+\{0,2\}\) the diamond obtained by adding one diagonal. Then for every \(\beta>0\):

* If \(\alpha\geq 7/8\), \(P_D(\alpha,\beta)<P_{C_4}(\alpha,\beta)\): adding the edge suppresses endemic infection at **all** transmission strengths.
* If \(0<\alpha<7/8\), there is exactly one \(\beta_*(\alpha)>0\); the edge increases endemic infection for \(0<\beta<\beta_*\), preserves it at \(\beta=\beta_*\), and suppresses it for \(\beta>\beta_*\).
* Four vertices are the smallest connected simple graph permitting a strict decrease in stationary infection prevalence after adding one edge, at positive spontaneous infection and transmission rates.

The \(7/8\) boundary is sharp. For example, at \(\alpha=\beta=1\),
\[
P_{C_4}=\frac{270}{443},\qquad P_D=\frac{2366908}{3887983},\qquad P_D-P_{C_4}=-\frac{1215166}{1722376469}<0.
\]

## Assumptions and scope

The population is a fixed, labeled finite simple connected undirected graph with at least two vertices. States are subsets \(S\subseteq V(G)\) of infected vertices. Every infected vertex recovers independently at rate \(1\). A susceptible vertex \(v\) becomes infected at rate
\[
\alpha+\beta\sum_{u\in S:\,u\sim v}\frac1{d_G(u)},\qquad \alpha,\beta>0.
\]
Each infected vertex attempts infectious contacts at total rate \(\beta\), independently of its degree. Failed attempts to infect already infected neighbors do nothing. Spontaneous infections make the finite chain irreducible; hence its stationary distribution \(\pi_G\) is unique and \(P_G=\sum_S |S|\pi_G(S)/|V(G)|\). Crucially, when adding an edge, the transmission rate along a **pre-existing** edge incident to its endpoint can fall because the source degree increases. The theorem does not apply to per-edge constant transmission rates.

## Proof

Put \(a=\alpha\) and \(b=\beta\). For each graph, form the continuous-time generator \(Q_G\) on infected subsets from the above rates. Quotient by graph-automorphism orbits (six state orbits for \(C_4\), nine for \(D\)); the quotient is exact because the generator commutes with automorphisms. Replace one row of \(Q_G^\mathsf T\) by ones, solve the stationary equations, and weight each orbit by its infected fraction. All calculations use rational functions over \(\mathbb Q[a,b]\); the accompanying `verify.py` explicitly constructs the generators and independently repeats the stationary solution with the unquotiented \(16\)-state generators at specified rational parameters.

Exact elimination and cancellation yield
\[
P_D-P_{C_4}=-\frac{ab^2F(a,b)}{U(a,b)V(a,b)},\qquad F(a,b)=\sum_{k=0}^8 c_k(a)b^k,
\]
where \(U,V\) are the two denominator polynomials returned by the reduced stationary systems, with **all coefficients strictly positive**, so \(U,V>0\) for \(a,b>0\). Their full coefficients and the identity are reconstructed by `verify.py` from the Markov generators, without relying on a numerical fit. The numerator coefficients are
\[
\begin{aligned}
c_0&=486(a+1)^8(8a-7),\\
c_1&=27(a+1)^6(684a^2+5a-337),\\
c_2&=3(a+1)^4(12438a^3+11505a^2-3359a-3143),\\
c_3&=(a+1)^2(41886a^4+79422a^3+33673a^2-8200a-4391),\\
c_4&=2(a+1)(14292a^4+27708a^3+14246a^2+589a-280),\\
c_5&=12152a^4+25111a^3+15356a^2+2683a+256,\\
c_6&=3146a^3+4047a^2+1127a+80,\\
c_7&=2a(227a+136),\\
c_8&=28a.
\end{aligned}
\]
Here each displayed coefficient \(c_0,\ldots,c_4\) has exactly one positive zero \(r_k\). Indeed, after discarding a strictly positive factor \((a+1)^j\), its remaining coefficient sequence has exactly one change of sign; negative constant and positive leading terms plus Descartes' rule yield uniqueness. Evaluations at rational endpoints establish
\[
r_4\in(1/10,1/8),\quad r_3\in(3/10,1/3),\quad r_2\in(1/2,3/5),\quad r_1\in(2/3,3/4),\quad r_0=7/8.
\]
In particular, \(r_4<r_3<r_2<r_1<r_0\). When \(a\ge r_0\), all nine \(c_k\ge0\) and \(c_5>0\), so \(F>0\) at all \(b>0\). When \(0<a<r_0\), the sequence \(c_0(a),\ldots,c_8(a)\), after zeros are omitted, has exactly one sign change, from negative to positive. Descartes' rule gives at most one positive root of \(F(a,\cdot)\); because its constant coefficient is negative and its leading coefficient is positive, continuity supplies at least one. The unique root is a genuine sign crossing; the sign of the displayed stationary difference gives the asserted phase diagram.

For the minimality claim, a connected graph on at most three vertices admits an added edge preserving its vertex set only in the path-to-triangle transition \(P_3\to K_3\). Exact analogous stationary elimination gives
\[
P_{K_3}-P_{P_3}=\frac{ab^2(2a+b+1)(2a+b+2)(2a^2+ab+4a+2)}{U_3(a,b)V_3(a,b)}>0,
\]
where \(U_3,V_3\) are denominator factors with entirely positive coefficients, also checked from the actual three-vertex generators in `verify.py`. The four-vertex example therefore realizes the smallest possible edge-induced suppression.

## Verification

Run `python3 verify.py` with Python 3 and SymPy. The script reconstructs the finite Markov generators from the precise state transition rates, computes exact rational stationary solutions after graph-symmetry reduction, verifies the numerator identity and positivity of every denominator coefficient, checks the strict rational root brackets and positive-root sign patterns, verifies the three-vertex expression, and compares the quotient systems against the independently constructed full \(16\)-state stationary systems for five rational parameter pairs. The universal root classification follows from Descartes' rule and analytic sign arguments, not from sampling the parameter plane. Exact mathematical status is limited to the stated finite models.

## Relationship to prior work

Gómez et al. (arXiv:0907.1313v1, publicly posted 2009-07-07) introduced contact-based epidemic models in which an infectious vertex's attempts are distributed among its neighbors; their equations (1)–(3) and discussion establish the source-degree mechanism. Their work uses discrete-time contact modeling and a probability/mean-field approximation rather than the present exact continuous-time finite-state stationary comparison with positive importation. Foxall (2014) treats spontaneous infection, transmission, and coupling monotonicity for generic pairwise rates. His standard coupling is not an edge-addition proof here: a new graph edge causes some existing directed pair rates to fall. Bartha, Komjáthy and Valesin (arXiv:2310.07040v1) investigate other degree-penalized contact processes, principally survival on growing random graphs; their symmetric degree penalties and main asymptotic questions do not state the present source-normalized four-site stationary phase threshold. The exact \(7/8\) threshold, unique crossing and sharp four-vertex boundary are the claim, not the underlying contact model or finite Markov techniques.

## Limitations

Stationary prevalence is a finite-state expectation, not a deterministic endemic equilibrium; spontaneous infection prevents absorption. The theorem compares specifically one cycle with one diagonal and establishes a smallest-size possibility, not an ordering for arbitrary networks or alternative infection rate normalizations. The original literature contains broad stochastic-process and degree-normalization frameworks, so historical priority may require wider specialist review. No human-independent validation is claimed.

## References

1. S. Gómez, A. Arenas, J. Borge-Holthoefer, S. Meloni and Y. Moreno, *Discrete-time Markov chain approach to contact-based disease spreading in complex networks*, arXiv:0907.1313v1 (2009-07-07), https://arxiv.org/abs/0907.1313.
2. E. Foxall, *Convergence and Monotonicity for a Model of Spontaneous Infection and Transmission*, Advances in Applied Probability (2014), DOI:10.1239/aap/1401369707.
3. A. Bartha, J. Komjáthy and D. Valesin, *Degree-penalized contact processes*, arXiv:2310.07040v1 (2023-10-10), https://arxiv.org/abs/2310.07040.
