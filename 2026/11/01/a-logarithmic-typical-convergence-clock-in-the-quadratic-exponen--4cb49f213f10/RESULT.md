# A logarithmic typical convergence clock in the quadratic-exponent Wielandt OR network

## Finding
For every integer \(n\ge3\), take the directed cycle \(0\to1\to\cdots\to n-1\to0\) and add the arc \(n-1\to1\). At each synchronous step, a vertex becomes active if at least one of its in-neighbors was active. Denote this disjunctive Boolean update by \(F_n\). Write \(T_n(x)\) for the least time at which \(F_n^t(x)\) is periodic, and for nonzero binary states \(x\), write \(L_n(x)\) for the largest number of consecutive zeros between active sites, cyclically. Set \(L_n(\mathbf1)=0\).

Every nonzero configuration reaches the all-one fixed point, and zero is the other fixed point. For every nonzero \(x\),
\[
T_n(x)\le nL_n(x),\qquad L_n(x)\ge2\implies n(L_n(x)-2)<T_n(x).
\]
In particular \(|T_n(x)-nL_n(x)|<2n\). The unique configuration with the maximum entry time is the single active vertex at \(0\), and
\[
\max_x T_n(x)=(n-1)^2+1.
\]
If \(X_n\) is uniformly distributed on \(\{0,1\}^n\), then
\[
\frac{T_n(X_n)}{n\log_2 n}\xrightarrow{\mathsf P}1,
\qquad
\frac{\mathbb E[T_n(X_n)]}{n\log_2 n}\longrightarrow1.
\]
Thus a network achieving the classical quadratic Wielandt exponent has a **linear-times-logarithmic typical relaxation clock**, controlled to within two full tours by the longest initial zero gap.

## Assumptions and scope
The state is a vector \(x=(x_0,\ldots,x_{n-1})\in\{0,1\}^n\); all updates are simultaneous. Explicitly,
\[
(F_nx)_0=x_{n-1},\qquad (F_nx)_1=x_0\lor x_{n-1},\qquad (F_nx)_j=x_{j-1}\quad(2\le j\le n-1).
\]
A time \(t=0\) is allowed when the starting state is already periodic. A cyclic zero gap of length \(L\) means \(L\) consecutive zero sites immediately following a one; for a nonzero state, \(0\le L\le n-1\). The all-zero state has entry time zero and is excluded from zero-gap inequalities. The random-state assertion uses independent fair Bernoulli coordinates, equivalently uniform configurations. All asymptotics are as \(n\to\infty\) through integers.

## Proof
**1. Boolean path representation and fixed points.** Let \(S\) be the set of initially active vertices. After \(t\) updates, the active set is exactly the set of endpoints of length-\(t\) directed walks from \(S\). This follows by induction and is equivalent to raising the adjacency matrix over the Boolean semiring. The digraph is strongly connected and has directed cycles of lengths \(n\) and \(n-1\), with gcd one. Consequently its Boolean adjacency matrix is primitive: for all sufficiently large \(t\), every ordered pair admits a walk of length \(t\). Hence every nonempty \(S\) ultimately fills the graph. The empty configuration remains empty. These are precisely the periodic states, both fixed.

**2. Upper comparison with cyclic gap length.** Let \(R\) denote the cyclic forward shift of active sets. There is a length-\(n\) directed walk from every vertex back to itself, following the Hamiltonian cycle. There is also a length-\(n\) walk from every \(i\) to \(i+1\pmod n\): follow the base cycle for \(n+1\) edge-steps, and replace one occurrence of \(n-1\to0\to1\) by the one-edge shortcut \(n-1\to1\). Every base walk of length \(n+1\) contains such an occurrence. Therefore, as Boolean operators, \(F_n^n\ge I\lor R\). Repeating and using distributivity gives
\[
F_n^{nk}\ge I\lor R\lor\cdots\lor R^k\qquad(k\ge0).
\]
For nonempty \(S\), the cyclic forward intervals of length \(L_n(x)+1\) starting at the vertices in \(S\) cover all \(n\) vertices. Thus \(F_n^{nL_n(x)}(x)=\mathbf1\), establishing \(T_n(x)\le nL_n(x)\). When \(L_n(x)=0\), the state is already all ones.

**3. Lower comparison via shortcut counts.** A length-\(t\) walk using \(s\) shortcuts advances \(t+s\pmod n\) vertices along the base cycle: ordinary edges advance one, while the shortcut advances two. Between successive shortcuts at least \(n-1\) edges must be traversed, and the first shortcut cannot occur before step one. Hence any walk with \(s\ge1\) shortcuts has length at least \(1+(s-1)(n-1)\). Let \(L=L_n(x)\ge2\) and put \(k=L-2\le n-3\). A walk of length \(nk\) cannot use \(k+2\) shortcuts, since that would require at least \(1+(k+1)(n-1)=nk+(n-k)>nk\) edges. Every site reachable after \(nk\) steps therefore lies among \(0,1,\ldots,k+1\) forward cyclic positions from a site in \(S\). The final zero in a gap of length \(L=k+2\) lies outside those intervals, so \(F_n^{nk}(x)\ne\mathbf1\). Therefore \(T_n(x)>n(L-2)\). Combining both estimates gives the claimed uniform error smaller than \(2n\) (also for \(L=0,1\)).

**4. The exact extreme and its unique initial state.** Put \(H=\{an+b(n-1):a,b\in\mathbb Z_{\ge0}\}\). Since \(n\) and \(n-1\) are coprime, the elementary two-generator Frobenius theorem says that the largest integer outside \(H\) is \(g=n(n-1)-n-(n-1)=n^2-3n+1\). Starting from \(e_0\), a walk reaching vertex \(j\in\{1,\ldots,n-1\}\) has length exactly \(j+h\) for some \(h\in H\), and every such length is achievable, by inserting loops of lengths \(n\) and \(n-1\). Positive walks from vertex \(0\) back to vertex \(0\) have length exactly \(n+h\) for \(h\in H\): the final return to zero uses the full cycle, with arbitrary full and short loops beforehand.

Set \(t_*=(n-1)^2+1\). For \(1\le j\le n-1\), we have \(t_*-j\ge g+2\in H\) in the sense that every integer at least \(g+1\) belongs to \(H\). Also \(t_*-n=g+1\in H\). Thus \(F_n^{t_*}(e_0)=\mathbf1\). But \(t_*-1-n=g\notin H\); the vertex \(0\) is inactive at time \(t_*-1\), proving \(T_n(e_0)=t_*\).

For \(0\le i\le n-1\), the first \(i\) iterates of \(e_0\) are exactly \(e_i\), because no shortcut has yet been encountered. Once all ones is reached it stays there, hence \(T_n(e_i)=t_*-i\). By monotonicity of the OR network, every initial nonempty state containing \(e_i\) reaches all ones no later than \(e_i\). Any state other than \(e_0\) with nonempty support contains some \(e_i\) with \(i\ge1\), so it has entry time at most \(t_*-1\). The zero state is already fixed. Therefore \(e_0\) is the unique maximizer.

**5. Typical time.** Let \(L_n\) denote the longest cyclic run of zeros in a fair Bernoulli word of length \(n\), setting \(L_n=n\) on the all-zero word for this probabilistic step. For any \(\varepsilon>0\), a union bound over the \(n\) cyclic starting positions yields
\[
\Pr(L_n\ge \lceil(1+\varepsilon)\log_2 n\rceil)\le n\,2^{-\lceil(1+\varepsilon)\log_2 n\rceil}\to0.
\]
For \(m=\lfloor(1-\varepsilon)\log_2 n\rfloor\), divide the first \(\lfloor n/m\rfloor m\) sites into \(\lfloor n/m\rfloor\) disjoint blocks of length \(m\). If any block is all zeros, then \(L_n\ge m\); independence gives
\[
\Pr(L_n<m)\le(1-2^{-m})^{\lfloor n/m\rfloor}\to0.
\]
Thus \(L_n/\log_2 n\to1\) in probability. The uniform \(2n\) error from steps 2–3 applies except to the all-zero state, which has probability \(2^{-n}\). It gives \(T_n/(n\log_2 n)\to1\) in probability.

For expectations, the same upper union bound and the tail-sum formula imply \(\mathbb E L_n\le \log_2 n+O(1)\), while the lower block bound implies \(\liminf\mathbb E L_n/\log_2 n\ge1\). Hence \(\mathbb E L_n\sim\log_2 n\). Removing the all-zero event changes \(\mathbb E L_n\) by at most \(n2^{-n}\). The deterministic upper and lower estimates then sandwich \(\mathbb E T_n\) between \(n\mathbb E L_n-O(n)\) and \(n\mathbb E L_n\), yielding the asserted expectation limit.

## Verification
Run `python3 verify.py` with Python 3.8 or later. The included script uses two independently coded update implementations. It exhaustively checks every one of the \(32{,}760\) labelled states for \(3\le n\le14\), verifies the gap bounds and uniqueness of the worst-case state, checks all singleton stopping times, and tests the key \(n\)-step Boolean walk inclusion for \(3\le n<90\). Its recorded output is in `verification_output.txt`, ending with `WIELANDT_OR_ALL_CHECKS_PASSED`. These finite checks do not establish the infinite-family or probabilistic assertions; those depend on the arguments above.

## Relationship to prior work
Wielandt's classical exponent bound and its extremal directed graph explain the quadratic worst-case scale; that worst-case bound is **not** asserted to be new. Jarrah, Laubenbacher and Veliz-Cuba (arXiv:0805.0275v1, 2 May 2008), especially Section 2 and Theorem 2.10, relate Boolean-network height to primitive-matrix exponents and determine the attractor structure for strongly connected conjunctive/disjunctive networks. Gadouleau (arXiv:2104.04403, 2021), especially Section 3.1.2, reviews the same periodic-point structure and existing height bounds. Neufeld and Shen (1998) study generalized exponents depending on the initial active set size, a closer comparison than the ordinary exponent; the accessible abstract does not state the longest-zero-gap bound or uniform-state logarithmic asymptotic, although its unavailable full text remains a residual equivalence risk.

The contribution assessed here is the *configuration-sensitive two-tour comparison* and the resulting exact leading constant for typical convergence, despite the pre-existing quadratic worst-case exponent. Cardinality-only generalized exponent bounds can remain quadratic for random initial supports of density about one half, so they do not by themselves establish this logarithmic-gap phenomenon.

## Limitations
The theorem applies only to the specified directed cycle with a shortcut from the penultimate vertex to vertex \(1\), synchronous OR updates, and fair independent initial colors for the probabilistic conclusion. It makes no claim about arbitrary primitive digraphs, other shortcuts, or general monotone networks. The deterministic estimate has an additive window smaller than \(2n\) and does not give an exact first-entry census for every initial configuration. The quadratic worst-case exponent is classical. Exhaustive literature equivalence is not proved; the full text of the 1998 generalized-exponent article was not accessible during review.

## References
- A. S. Jarrah, R. Laubenbacher, and A. Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, arXiv:0805.0275v1 (first public posting 2008-05-02), https://arxiv.org/pdf/0805.0275.
- M. Gadouleau, *Dynamical properties of disjunctive Boolean networks*, arXiv:2104.04403 (2021), https://arxiv.org/pdf/2104.04403.
- S. Neufeld and J. Shen, *Some results on generalized exponents*, Journal of Graph Theory **28** (1998), 215–225, DOI:10.1002/(SICI)1097-0118(199808)28:4<215::AID-JGT3>3.0.CO;2-M.
- R. A. Brualdi and B. Liu, *Generalized exponents of primitive directed graphs*, Journal of Graph Theory **14** (1990), 483–499, DOI:10.1002/jgt.3190140413.
- S. J. Kirkland, D. D. Olesky, and P. van den Driessche, *Digraphs with large exponent*, Electronic Journal of Linear Algebra **7** (2000), 30–40, DOI:10.13001/1081-3810.1044.
