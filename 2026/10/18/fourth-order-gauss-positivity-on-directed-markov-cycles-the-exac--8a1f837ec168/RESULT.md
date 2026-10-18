# Fourth-order Gauss positivity on directed Markov cycles: the exact all-step classification

## Finding

Let \(n\ge2\). On the directed cycle with state indices \(0,\ldots,n-1\), give the edge \(i\to i+1\pmod n\) an arbitrary positive rate \(q_i\). Write \(Q_{ii}=-q_i\), \(Q_{i,i+1}=q_i\), and all other entries zero (the two entries are understood at distinct columns, including when \(n=2\)). Consider the two-stage fourth-order Gauss–Legendre time integrator, whose end-step matrix is

\[
T(h)=R(hQ),\qquad R(z)=\frac{12+6z+z^2}{12-6z+z^2},\qquad h\ge0.
\]

**Theorem.** The matrix \(T(h)\) is entrywise nonnegative for **every** \(h\ge0\) if and only if either (i) \(n=2\), without restrictions on the two positive rates, or (ii) \(n=3\) and all three rates coincide. In these two cases \(T(h)\) is strictly positive for \(h>0\). For every other rate-labeled cycle there is an off-diagonal entry of \(T(h)\) that is strictly negative for all sufficiently large \(h\).

A quantitative strengthening holds for every \(n\ge4\). Set \(s_i=q_i^{-1}\), \(S=\sum_i s_i\), and let \(\mathcal N\) be the set of unordered pairs of nonadjacent vertices of the undirected \(n\)-cycle. Then

\[
\boxed{\lim_{h\to\infty}h\sum_{j=0}^{n-1}T(h)_{j-1,j}=-\frac{12}{S}\sum_{\{i,j\}\in\mathcal N}s_i s_j<0.}
\]

Indices in matrix entries are cyclic, so \(j-1\) means \(j-1\pmod n\). The strict inequality shows that at least one forward-neighbor probability eventually becomes negative, irrespective of rate heterogeneity.

For the equal-rate four-cycle, with common rate \(q>0\) and \(x=hq\), there is an **exact** one-sided timestep threshold:

\[
\boxed{T(h)\ge0\ \Longleftrightarrow\ 0\le x\le\rho,\qquad
\rho\approx6.13572028261049,}
\]

where \(\rho\) is the unique positive real root of \(x^4-24x^2-72x-72=0\). The threshold statement is particular to the uniform four-cycle; no assertion that arbitrary cycles have a single positivity interval is made.

## Assumptions and scope

The generator \(Q\) is a conservative **row** generator: \(Q\mathbf1=0\) and its only positive off-diagonal entries are the forward directed-cycle edges. Every \(q_i\) is real and strictly positive, so the finite chain is irreducible. Nonnegativity of a matrix is entrywise and is distinguished from the automatic conservation law \(T(h)\mathbf1=\mathbf1\). Neither reversibility nor symmetric edge weights is assumed. The assertion concerns a single Gauss–Legendre step, not internal-stage positivity or an arbitrary multistep composition.

The rational matrix function is well defined for all \(h\ge0\): the denominator polynomial has roots \(3\pm i\sqrt3\), with strictly positive real parts, while all eigenvalues of a finite Markov generator have nonpositive real parts. The scalar stability function above is the classical \([2/2]\) diagonal Padé approximation to the exponential.

## Proof

**1. A group-inverse expression for the large-step sign.** Put \(s_i=1/q_i\), \(S=\sum_i s_i\), and \(\pi_j=s_j/S\). The stationary projector is \(\Pi=\mathbf1\pi\). Define the directed travel-time sums \(m_{ij}\) by \(m_{ii}=0\) and, for \(i\ne j\),

\[
m_{ij}=s_i+s_{i+1}+\cdots+s_{j-1},
\]

where the indices follow the forward directed arc from \(i\) to \(j\) and the target's holding time is excluded. In particular, for distinct vertices \(i,j\),

\[
m_{ij}+m_{ji}=S.
\]

Define

\[
G_{ij}=\pi_j\left(m_{ij}-\sum_k\pi_k m_{kj}\right).
\]

For fixed \(j\), the vector \(m_{\bullet j}\) obeys \(Qm_{\bullet j}=\pi_j^{-1}e_j-\mathbf1\). Consequently, \(QG=I-\Pi\) and \(\pi G=0\). Since \(Q+\Pi\) is invertible (irreducibility), these identities imply

\[
G=(Q+\Pi)^{-1}-\Pi,
\quad GQ=QG=I-\Pi,\quad G\mathbf1=0.
\]

Thus \(G\) is the group inverse of \(Q\), using the generator's sign convention. On the stationary one-dimensional subspace \(R(hQ)=I\); on its complement \(Q\) is invertible. The resolvent identity

\[
R(hQ)=I+12hQ(12I-6hQ+h^2Q^2)^{-1}
\]

therefore yields, entrywise and for fixed positive rates,

\[
T(h)=I+\frac{12}{h}G+O(h^{-2})\qquad(h\to\infty).
\]

The \(O(h^{-2})\) coefficient depends on the fixed generator; no uniformity over degenerating rates is claimed. Every strictly negative off-diagonal entry of \(G\) consequently creates a strictly negative entry of \(T(h)\) for all sufficiently large \(h\).

**2. Four or more states.** Summing the entries just preceding the target vertex gives

\[
\begin{aligned}
\sum_jG_{j-1,j}
&=\sum_j\pi_j s_{j-1}-\sum_{i,j}\pi_i\pi_j m_{ij}\\
&=\frac1S\left(\sum_j s_js_{j-1}-\sum_{i<j}s_is_j\right).
\end{aligned}
\]

The second equality uses \(m_{ij}+m_{ji}=S\). When \(n\ge4\), the unordered pairs \(\{j-1,j\}\) are precisely the \(n\) distinct edges of the underlying undirected cycle. All remaining unordered pairs are the nonadjacent pairs \(\mathcal N\). Therefore

\[
\sum_jG_{j-1,j}=-\frac1S\sum_{\{i,j\}\in\mathcal N}s_is_j<0.
\]

Since \(\mathcal N\) is nonempty for every \(n\ge4\), at least one term is negative; multiplying the large-step expansion by \(h\), summing, and taking the limit proves both the quantitative formula and the impossibility of unconditional nonnegativity.

**3. Three states.** For \(n=3\), the same aggregate expression is zero because every unordered pair is an edge. The individual entries simplify to

\[
G_{j-1,j}=\frac{s_j}{S^2}\left(s_js_{j-1}-s_{j+1}^2\right).
\]

If the three rates are unequal, the three numbers displayed cannot all be nonnegative: they sum to zero, so simultaneous nonnegativity would force each to be zero. The resulting three equalities \(s_js_{j-1}=s_{j+1}^2\) imply \(s_0=s_1=s_2\) by positivity (divide consecutive equalities). Hence heterogeneous three-cycles have a negative off-diagonal entry of \(G\), and thus lose nonnegativity at all sufficiently large steps.

Conversely, when all three rates equal \(q>0\), let \(x=hq\). Direct multiplication in the three-dimensional circulant algebra shows that every row of \(T(h)\) is a cyclic shift of

\[
\left(
\frac{x^2-2x+4}{x^2+2x+4},\quad
\frac{8x}{(x+2)(x^2+2x+4)},\quad
\frac{4x^2}{(x+2)(x^2+2x+4)}
\right).
\]

All three entries are positive whenever \(x>0\), because \(x^2-2x+4=(x-1)^2+3>0\).

**4. Two states.** The nonzero eigenvalue of \(Q\) is \(-\kappa\), where \(\kappa=q_0+q_1>0\). Thus

\[
T(h)=rI+(1-r)\Pi,
\qquad r=\frac{(h\kappa)^2-6h\kappa+12}{(h\kappa)^2+6h\kappa+12}.
\]

For every \(h>0\), \(0<r<1\), since the numerator equals \((h\kappa-3)^2+3\) and the denominator exceeds it by \(12h\kappa\). As \(\Pi\) has strictly positive entries, so does \(T(h)\).

**5. A sharp four-state threshold.** On the uniform four-cycle the first row of \(T(h)\), again writing \(x=hq\), has common positive denominator

\[
D=2(x^2+3x+3)(x^4+6x^3+18x^2+36x+36)
\]

and numerators, in cyclic order,

\[
\begin{aligned}
N_0&=2x^6+9x^5+6x^4+72x^2+216x+216,\\
N_1&=-3x(x^4-24x^2-72x-72),\\
N_2&=3x^2(x^3+12x^2+36x+36),\\
N_3&=9x^3(x+2)^2.
\end{aligned}
\]

For \(x>0\), all these expressions except possibly \(N_1\) are strictly positive. The quartic \(f(x)=x^4-24x^2-72x-72\) has exactly one positive real zero: its ordered nonzero coefficient signs have exactly one variation, \(f(0)<0\), and \(f(x)\to+\infty\). Therefore \(N_1\ge0\) exactly for \(0\le x\le\rho\). Circulant symmetry gives the stated complete four-state positivity set. This completes the proof.

## Verification

Run `python -m pip install -r requirements.txt` and then `python verify.py` in the same directory as this document. The standalone exact-arithmetic program checks the hitting-time group inverse against both matrix identities for three positive rate patterns at each order \(2\le n\le8\); checks cyclic aggregate negativity and the three-state formulas; verifies exact row sums and the rational resolvent identity at several positive rational steps; and symbolically reconstructs the full equal-rate three- and four-state circulant transition matrices and the unique positive four-cycle threshold. An example heterogeneous triangle with rates \((1,2,3)\) has \(G_{1,2}=-10/121\), so its \((1,2)\) transition coefficient is \(-120/(121h)+O(h^{-2})\).

The verifier is corroborating finite exact computation, not an exhaustive enumeration of all positive rates or an infinite-family computer proof. The mathematical conclusion for all dimensions and all positive rates is established by the identities and inequalities in the preceding sections.

## Relationship to prior work

The scalar \([2/2]\) Padé stability function and general limitations of Padé discretizations on positive linear systems are established background. Zappavigna, Colaneri, Kirkland and Shorten (2010) provide examples of positivity failure and sufficient conditions for positivity; their 2012 treatment explicitly introduces a cyclic Metzler feedback matrix, and specializes a counterexample to an open, nilpotent chain. The present statement does **not** claim discovery of Padé positivity failure, cyclic generators or generalized-inverse methods. It gives instead the **complete all-step equivalence for irreducible rate-labeled cycles**, its strict nonadjacent-pair asymptotic obstruction, and the exact four-cycle timestep frontier. Those particular conclusions are not stated in the inspected relevant sections of these antecedents.

The group-inverse and mean-first-passage formulation is classical and is used here as a proof technique, not as an originality claim. General sufficient sampling-time conditions do not by themselves imply an exact all-parameter and all-timestep classification; conversely this special cycle theorem does not extend such conditions to arbitrary positive systems.

## Limitations

The classification assumes a *single, strongly connected, forward-only* cycle with strictly positive rates. It does not classify general strongly connected digraphs, bidirectional ring generators, vanishing edge rates, nonconservative positive systems, internal Runge–Kutta stages or repeated products of different steps. For arbitrary nonuniform rates and \(n\ge4\), the proof establishes eventual negative entries, not an explicit earliest negative timestep or the topology of the full positivity-preserving timestep set. The exact four-cycle threshold applies only to homogeneous rates. Independent mathematical validation and a guaranteed exhaustive historical-literature determination have not been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, Proceedings of MTNS 2010, Budapest (2010). Open manuscript and date-resolved repository entry: https://mural.maynoothuniversity.ie/id/eprint/2195/ (deposited 2010-10-15).
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, preprint deposited 2012-06-19, subsequently published in Linear Algebra and its Applications. Lawful manuscript: https://mural.maynoothuniversity.ie/id/eprint/3761/ .
3. F. Rossi, P. Colaneri and R. Shorten, *Padé discretization for linear systems with polyhedral Lyapunov functions*, IEEE Transactions on Automatic Control **56** (2011), 2717–2722. DOI: 10.1109/TAC.2011.2161028; OA archive https://mural.maynoothuniversity.ie/id/eprint/2822/ .
