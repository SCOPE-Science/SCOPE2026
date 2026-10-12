# Full rank of long-time quantum mixing on primitive strongly regular graphs

## Finding
Let \(G\) be any finite simple primitive strongly regular graph on \(n\) vertices, where *primitive* means that both \(G\) and its complement are connected. With adjacency matrix \(A\), define the continuous-time quantum walk \(U(t)=\exp(itA)\) and its long-time mixing matrix
\[
\widehat M(G)=\lim_{T\to\infty}\frac1T\int_0^T U(t)\circ\overline{U(t)}\,dt.
\]
Then \(\widehat M(G)\) is **strictly positive definite**, and hence \(\operatorname{rank}\widehat M(G)=n\). This holds for every feasible primitive strongly regular graph, without requiring integral eigenvalues, vertex transitivity, or an instantaneous mixing time.

More quantitatively, write the adjacency eigenvalues as \(k>r>s\), where \(k\) is the degree. The nonprincipal long-time-mixing eigenvalue on the \(r\)-eigenspace is exactly
\[
\Lambda_r=\frac{r^2+s(s+2)}{(r-s)^2}-\frac{2r(s+1)}{(k-r)(r-s)}.
\]
For every such graph except the five-cycle, \(r\ge1\) and \(s\le-2\), making both terms nonnegative and the second strictly positive. The other nonprincipal mixing eigenvalue is obtained by applying this same expression to the complementary graph. For the five-cycle, both nonprincipal mixing eigenvalues equal \(1/5\).

## Assumptions and scope
A strongly regular graph has parameters \((n,k,\lambda,\mu)\): it is a simple \(k\)-regular graph; adjacent vertices have \(\lambda\) common neighbors and nonadjacent vertices have \(\mu\). We assume \(G\) and \(\overline G\) are connected. The matrices and all eigenvalues are real, and \(\circ\) denotes entrywise multiplication. This is the **ordinary uniform-in-time Cesàro average**, not mixing under an arbitrary sampling distribution. The conclusion concerns the ordinary matrix rank and the strict positivity of its eigenvalues; no claim is made for imprimitive strongly regular graphs or primitive distance-regular graphs of diameter greater than two.

## Proof
**1. Reduce the long-time average.** The standard spectral identity [1,2] gives
\[
A=kE_0+rE_r+sE_s,\quad E_0=\frac1nJ,\qquad
\widehat M=E_0\circ E_0+E_r\circ E_r+E_s\circ E_s.
\]
The three adjacency eigenspaces are mutually orthogonal. Since \(G\) is connected, \(E_0\) has rank one. Strong regularity gives
\[
A^2=(\lambda-\mu)A+(k-\mu)I+\mu J,
\quad r+s=\lambda-\mu,\quad rs=\mu-k.
\]
Put \(\ell=n-k-1>0\). The multiplicities \(m=\operatorname{rank}E_r\) and \(p=\operatorname{rank}E_s\) satisfy
\[
m=\frac{-k-(n-1)s}{r-s},\quad p=n-1-m,
\quad n=\frac{(k-r)(k-s)}{k+rs},
\]
where \(k+rs=\mu>0\). The projector entries are constant on the diagonal, edges, and nonedges:
\[
\begin{array}{c|ccc}
&u=v&u\sim v&u\not\sim v,\;u\ne v\\ \hline
E_0&1/n&1/n&1/n\\
E_r&m/n&mr/(nk)&-m(r+1)/(n\ell)\\
E_s&p/n&ps/(nk)&-p(s+1)/(n\ell)
\end{array}
\]
These entries follow directly from \(E_r=(A-sI-(k-s)J/n)/(r-s)\) and \(E_s=(rI-A+(k-r)J/n)/(r-s)\).

**2. Compute the nonprincipal mixing eigenvalues.** Let \(d,e,f\) be the respective diagonal, edge, and nonedge entries of \(\widehat M\). The preceding table yields
\[
\begin{aligned}
d&=(1+m^2+p^2)/n^2,\\
e&=(1+m^2r^2/k^2+p^2s^2/k^2)/n^2,\\
f&=(1+m^2(r+1)^2/\ell^2+p^2(s+1)^2/\ell^2)/n^2.
\end{aligned}
\]
Consequently \(\widehat M=(d-f)I+(e-f)A+fJ\). Since \(E_rJ=E_sJ=0\), its eigenvalues on the two restricted adjacency eigenspaces are \(\Lambda_r=d-f+(e-f)r\) and \(\Lambda_s=d-f+(e-f)s\). Substitute the displayed expressions for \(m,p,n,\ell\), and cancel. This gives exactly
\[
\boxed{\Lambda_r=\frac{r^2+s(s+2)}{(r-s)^2}-\frac{2r(s+1)}{(k-r)(r-s)}.}
\]
The cancellation is an identity of rational functions under the strongly regular parameter relations; the standalone symbolic checker reproduces it independently.

**3. Establish the required spectral signs.** For a primitive strongly regular graph, \(r>0\) and \(s<-1\). Indeed, \(r=0\) would give \(\mu=k\), making every pair of nonadjacent vertices false twins and the complement disconnected. Applying that argument to the connected complement, whose positive restricted eigenvalue is \(-1-s\), gives \(s<-1\).

If \(r,s\) are integers, it follows immediately that \(r\ge1\) and \(s\le-2\). Otherwise they are quadratic conjugates and their integer multiplicities are equal by Galois conjugation. Hence \(m=p=(n-1)/2\). From \(\operatorname{tr}A=0\), the integer \(r+s=-2k/(n-1)\) lies strictly between \(-2\) and \(0\), so \(r+s=-1\). Using \(\operatorname{tr}(A^2)=nk\) together with the strong regularity relation gives \(k=(n-1)/2\), \(\mu=(n-1)/4\), and
\[
r=\frac{\sqrt n-1}{2},\qquad s=-\frac{\sqrt n+1}{2},\qquad n\equiv1\pmod4.
\]
When \(n\ge9\), again \(r\ge1\) and \(s\le-2\). The only remaining possibility is \(n=5\), whose parameters force \(G=C_5\).

For \(r\ge1\), \(s\le-2\), the first term in the boxed formula is nonnegative and the second is strictly positive because \(0<r<k\), \(s+1<0\), and \(r-s>0\). Thus \(\Lambda_r>0\).

**4. Use complement symmetry, including the exceptional case.** Since \(A(\overline G)=J-I-A\), the complement has restricted eigenvalues \(\bar r=-1-s>0\) and \(\bar s=-1-r<-1\); its three spectral projectors are precisely the same projectors, with the two nonprincipal ones interchanged. Therefore \(\widehat M(\overline G)=\widehat M(G)\) exactly and \(\Lambda_s(G)=\Lambda_{\bar r}(\overline G)>0\). The exceptional \(C_5\) is self-complementary, and a direct substitution gives \(\widehat M(C_5)=(5I+4J)/25\), with eigenvalues \(1\) and \(1/5\) (multiplicity four). Finally, \(\widehat M\) is doubly stochastic, so its eigenvalue on constants is \(1\). Thus all eigenvalues of \(\widehat M\) are strictly positive, proving positive definiteness and full rank. \(\square\)

## Verification
The standalone file `verify.py` checks two general symbolic identities: the formula for \(\Lambda_r\) and its complementary formula for \(\Lambda_s\). It independently constructs the exact adjacency matrices of \(C_5\), the Petersen graph and its complement, and the rook graphs on \(3\times3\) and \(4\times4\) grids. For each, it reconstructs the strongly regular identity, spectral projectors, Schur-square mixing matrix, eigenvalue formulas, and full rank using exact SymPy arithmetic. Run `python verify.py` with the dependency listed in `requirements.txt`. These examples confirm the identities in selected cases; the proof's case division and strict inequalities establish the claim for every primitive strongly regular graph.

## Relationship to prior work
The spectral identity and the interpretation of \(\widehat M\) as a Gram matrix of time-averaged vertex states are established in [1,2]. In [3], the primitive distance-regular full-rank question is explicitly posed; the present theorem establishes its diameter-two (strongly regular) case only. The contemporary study [4] gives an exact moment analysis of freely selected observation-time distributions on strongly regular graphs and the three-projector expansion, but addresses uniform averaging under chosen laws rather than positive definiteness of the fixed long-time Cesàro average. None of these general formulas alone supplies the strict two-eigenvalue sign argument required here. The rank claim is distinct from uniform mixing at a selected time or under a selected law.

## Limitations
There is no classification of larger-diameter distance-regular graphs here, no characterization of arbitrary observation-time laws, and no claim about a minimum positive eigenvalue bounded independently of graph parameters. Strong regularity and connectedness of the complement are essential assumptions of the proof. The numerical examples are not an exhaustive census of parameter sets. While the checked sources do not contain the universal positive-definiteness statement for primitive strongly regular graphs, differently indexed treatments or deductions from additional Krein-parameter theory remain possible.

## References
[1] G. Coutinho, C. Godsil, K. Guo, H. Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591 (first posted 2017-09-11), §§1, 3–5.

[2] G. Coutinho, P. F. Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational Quantum Walks*, arXiv:2208.08971 (first posted 2022-08-18), §2.

[3] G. Coutinho, K. Guo, *Selected Open Problems in Continuous-Time Quantum Walks*, arXiv:2404.02236 (first posted 2024-04-02), §4 and Open Problem 4.1 of the initial preprint.

[4] M. Kang, *Moment Methods for Uniform Average Mixing on Strongly Regular Graphs*, arXiv:2610.10017 (first posted 2026-10-07), §§1–2, 7; consulted for comparison only, not for cohort dating.
