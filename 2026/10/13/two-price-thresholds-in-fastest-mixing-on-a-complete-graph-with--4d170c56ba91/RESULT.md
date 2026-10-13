# Two price thresholds in fastest mixing on a complete graph with a costly clique

## Finding

Let \(s,r\ge2\) be integers, \(n=s+r\), and distinguish a set \(A\) of \(s\) vertices from its \(r\)-vertex complement \(B\) in the complete graph \(K_n\). An edge within \(A\) has positive unit conductance price \(t>0\); all cross-edges and all edges within \(B\) have unit price. With nonnegative symmetric edge rates and budget one, maximize the second eigenvalue \(\lambda_2\) of the combinatorial weighted Laplacian.

There is a globally optimal allocation constant on each of the three edge classes. Let its three rates be \(a\) (within \(A\)), \(b\) (between \(A,B\)), and \(c\) (within \(B\)). Write
\[
\tau_1=\frac{s(r+1)}{r(s-1)},\qquad \tau_2=\frac{2s}{s-1},\qquad
D(t)=t\binom{s}{2}+sr+\binom r2.
\]
Both thresholds exceed one; if \(s>r\), then \(\tau_1<\tau_2\). All values below are exact.

**Regime I (every \(s,r\)):** If \(0<t<\tau_1\), an optimal allocation has identical rates \(a=b=c=1/D(t)\), and the optimal gap is \(n/D(t)\). It is the only optimal allocation invariant under all permutations within \(A\) and within \(B\).

**Regime IIa (\(s\le r\)):** If \(t>\tau_1\), define
\[
C_{\mathrm{IIa}}=s+\frac{(r-1)(r-s)}{2r}.
\]
An optimal allocation has \(a=0\), \(b=1/(rC_{\mathrm{IIa}})\), \(c=(r-s)/(r^2C_{\mathrm{IIa}})\), and optimal gap \(1/C_{\mathrm{IIa}}\), independent of \(t\). These are the unique optimal orbit-constant rates.

**Regime IIb (\(s>r\)):** If \(\tau_1<t<\tau_2\), define
\[
C_{\mathrm{IIb}}(t)=r+\frac{t(s-1)(s-r)}{2s}.
\]
An optimal allocation has \(a=(s-r)/(s^2C_{\mathrm{IIb}}(t))>0\), \(b=1/(sC_{\mathrm{IIb}}(t))>0\), and \(c=0\); the gap is \(1/C_{\mathrm{IIb}}(t)\). These are the unique optimal orbit-constant rates. In particular, **all less-expensive edges within \(B\) are optimally deleted while the costly edges within \(A\) remain present**.

**Regime III (\(s>r\)):** If \(t>\tau_2\), the unique optimal orbit-constant allocation has \(a=c=0\), \(b=1/(sr)\), and gap \(1/s\). The optimal network can be chosen to be the complete bipartite graph \(K_{s,r}\).

At the transition prices the adjacent gap formulas coincide, but orbit-constant optimizers need not be unique. The complete transition families are given in the proof. No uniqueness of arbitrary (not necessarily orbit-constant) optimal allocations is asserted.

## Assumptions and scope

The rates are nonnegative real numbers on *all* edges of \(K_n\) (zero means deletion), with exact budget
\[
t\sum_{\{i,j\}\subset A}w_{ij}
+\sum_{i\in A,j\in B}w_{ij}
+\sum_{\{i,j\}\subset B}w_{ij}=1.
\]
The generator of the symmetric continuous-time Markov process is \(-L(w)\); \(L(w)\) is the unnormalized combinatorial Laplacian. Its second-smallest eigenvalue is the asymptotic decay rate to the uniform equilibrium distribution. This is not the discrete-time second-largest-eigenvalue-modulus problem. The theorem covers every integer \(s,r\ge2\) and every real \(t>0\), without generic-position restrictions.

## Proof

**1. An optimal orbit-constant allocation exists.** The feasible set is compact and contains connected positive-rate networks. On the orthogonal complement of the constant vector,
\[
\lambda_2(L(w))=\min_{x\perp\mathbf1,\ \|x\|_2=1}\;x^{\mathsf T}L(w)x
\]
is concave in \(w\). The edge prices and constraints are invariant under \(S_s\times S_r\), the group of permutations inside the two vertex classes. Averaging any maximizer over this group preserves its budget and cannot decrease \(\lambda_2\). The average has three rates \(a,b,c\ge0\), one on each edge orbit.

**2. Complete spectrum of an orbit-constant design.** Decompose \(\mathbb R^n\) orthogonally into the constants (dimension one); vectors supported on \(A\) with zero sum (dimension \(s-1\)); vectors supported on \(B\) with zero sum (dimension \(r-1\)); and the class-constant contrast vector (dimension one). Direct Laplacian multiplication gives eigenvalues
\[
0,\quad sa+rb\quad(s-1\text{ times}),\quad
sb+rc\quad(r-1\text{ times}),\quad nb\quad(1\text{ time}).
\]
Therefore
\[
\lambda_2(L(a,b,c))=\min\{sa+rb,\ sb+rc,\ nb\},\qquad
\mathcal B(a,b,c)=t\binom{s}{2}a+sr b+\binom r2c.
\]
The three spectral inequalities are exact, not estimates.

**3. Reciprocal minimum-cost problem.** By positive homogeneity, maximize the gap under \(\mathcal B=1\) by first minimizing \(\mathcal B\) subject to \(\lambda_2\ge1\), then scaling all rates by the reciprocal of that minimum cost. Given \(b\ge1/n\), the least feasible \(a\) and \(c\), because both prices are strictly positive, are
\[
a_0(b)=\frac{(1-rb)_+}{s},\qquad
c_0(b)=\frac{(1-sb)_+}{r},\qquad
(u)_+=\max\{u,0\}.
\]
The remaining exact one-variable cost is
\[
F_t(b)=sr b+\frac{t(s-1)}2(1-rb)_+
+\frac{r-1}2(1-sb)_+,\qquad b\ge1/n.
\]
Above both breakpoints \(1/s\) and \(1/r\), \(F_t\) increases strictly. Thus only the intervals ending at those two points need consideration.

For \(s\le r\), the derivatives on successive intervals, beginning at \(1/n\), are
\[
F_t'(b)=\begin{cases}
\frac12[s(r+1)-tr(s-1)],&1/n<b<1/r,\\
\frac{s(r+1)}2,&1/r<b<1/s,\\
sr,&b>1/s.
\end{cases}
\]
The two latter derivatives are strictly positive. The first changes sign exactly at \(\tau_1=s(r+1)/(r(s-1))\). Therefore the unique minimizing \(b\) is \(1/n\) below \(\tau_1\), and \(1/r\) above it. At equality *every* \(b\in[1/n,1/r]\) minimizes the cost. For \(s=r\), the intermediate interval is empty, and the same conclusion holds.

For \(s>r\), the derivatives are
\[
F_t'(b)=\begin{cases}
\frac12[s(r+1)-tr(s-1)],&1/n<b<1/s,\\
\frac r2[2s-t(s-1)],&1/s<b<1/r,\\
sr,&b>1/r.
\end{cases}
\]
Because \(r\ge2\), \(\tau_1<\tau_2\). Consequently the unique minimizing \(b\) is \(1/n\) for \(t<\tau_1\), \(1/s\) for \(\tau_1<t<\tau_2\), and \(1/r\) for \(t>\tau_2\). At \(t=\tau_1\) all \(b\in[1/n,1/s]\) minimize, while at \(t=\tau_2\) all \(b\in[1/s,1/r]\) minimize. These are complete sets of minimizers *within the orbit-constant class*.

**4. Values, rates, and boundaries.** Substitute each minimizing \(b\) into \(a_0(b),c_0(b)\), and rescale by \(1/F_t(b)\). At \(b=1/n\), the unscaled triple is \((1/n,1/n,1/n)\), its cost is \(D(t)/n\), and rescaling gives the regime-I formulas. At \(b=1/r\) with \(s\le r\), the triple is \((0,1/r,(r-s)/r^2)\) and its cost is \(C_{\mathrm{IIa}}\). At \(b=1/s\) with \(s>r\), the triple is \(((s-r)/s^2,1/s,0)\) and its cost is \(C_{\mathrm{IIb}}(t)\). At \(b=1/r\) with \(s>r\), the triple is \((0,1/r,0)\) and its cost is \(s\). Each has spectral gap exactly one before scaling, as at least one of the eigenvalues from step 2 equals one. This also proves that all stated objective values are exact. The minimizing-interval argument supplies every equality case stated above, and strict monotonicity off those intervals proves uniqueness within the orbit-constant class away from the thresholds. \(\square\)

## Verification

An accompanying standalone Python script (`verify.py`) uses exact rational arithmetic to check the budget, complete eigenvalue decompositions via direct weighted-Laplacian multiplication, and the optimal breakpoint inequalities for 955 combinations with \(2\le s,r\le10\) and prices including both thresholds and nearby rational values. An additional non-packaged numerical sanity check compared 4,200 unrestricted positive edge-budget allocations with the theorem's optimum on selected small cases; none exceeded it. The proof above, rather than finite testing, establishes the arbitrary-dimensional and real-price claims.

For a concrete intermediate example, take \(s=4,r=2,t=7/3\). Then \(\tau_1=2\), \(\tau_2=8/3\), and the unique orbit-constant optimum has \((a,b,c)=(1/30,1/15,0)\) and optimal gap \(4/15\). The comparatively cheap edge within the two-vertex class is deleted, although every expensive edge within the four-vertex class remains.

## Relationship to prior work

Sun, Boyd, Xiao, and Diaconis [1] formulate optimal continuous-time graph mixing under general positive linear edge prices as a semidefinite problem and develop its geometric dual. Their full-text examples treat a particular small graph, paths, and cycles; the present phase thresholds and the counterintuitive priced-clique deletion order are not supplied by those examples or by a numerical SDP specification.

Boyd, Diaconis, Parrilo, and Xiao [2] give rigorous graph-symmetry reduction and block diagonalization for the *discrete-time* fastest-mixing Markov chain with a second-largest-eigenvalue-modulus objective. Symmetry averaging in step 1 is standard; the priced-clique *continuous-time* eigenvalue and breakpoint solution in steps 2–4 is the specific contribution assessed here.

Shakeri and coauthors [3] identify spectral transition behavior in a two-layer interconnection problem. They hold each internal layer fixed and optimize only one-to-one interlayer edges, whereas here *all* within-layer and all-to-all cross-edge rates share a price budget. The two optimization problems are not equivalent, and the formulas of one do not specialize to those of the other. No claim is made that spectral-gap optimization, symmetry averaging, or semidefinite formulations are new.

## Limitations

The classification concerns the maximum second Laplacian eigenvalue, not all eigenvalues, discrete-time mixing, robustness, or other optimization criteria. The rates and transition families completely classify **orbit-constant** optima; other non-invariant optimal allocations may exist and are not classified. No claim about an independently verified literature priority or independent audit is made. A differently formulated older theorem for a two-price complete graph could remain outside the consulted literature.

## References

1. J. Sun, S. Boyd, L. Xiao, and P. Diaconis, “The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem,” *SIAM Review* 48 (2006), 681–699. DOI: 10.1137/S0036144504443821. Public electronic date verified as 2006-11-02 from the article's first page.
2. S. Boyd, P. Diaconis, P. A. Parrilo, and L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” arXiv:0709.0955, v1 dated 2007-09-06; *SIAM Journal on Optimization* 20 (2009), 792–819.
3. H. Shakeri, N. Albin, F. D. Sahneh, P. Poggi-Corradini, and C. Scoglio, “Maximizing Algebraic Connectivity in Interconnected Networks,” arXiv:1510.06785, v1 dated 2015-10-22.
