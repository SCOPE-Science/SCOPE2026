# A sharp disagreement window between resistance-maximal and coherence-optimal leader pairs

## Finding
Consider the six-vertex weighted, undirected circulant network on \(\mathbb Z/6\mathbb Z\) with conductance \(10\) on cyclic-distance-one edges, conductance \(1\) on cyclic-distance-two edges, and conductance \(c>0\) on the three opposite-vertex edges (cyclic distance three). For two noise-free leaders \(S\), minimize the grounded-Laplacian coherence \(C(S)=\operatorname{tr}(L_{V\setminus S,V\setminus S}^{-1})\). Let \(R(S)\) be the electrical effective resistance between the leaders.

Put
\[
 c_R=-5+\frac32\sqrt{34},\qquad
 P(c)=10c^4+419c^3+4920c^2+4685c-146357,
\]
and let \(c_C\) be the unique positive zero of \(P\), so that \(3<c_R<4<c_C<5\). Each unordered leader pair has cyclic separation \(r\in\{1,2,3\}\). The complete classification is:

- For \(0<c<c_R\), the unique optimal separation for both maximum effective resistance and minimum coherence is \(r=3\).
- At \(c=c_R\), the resistance maximizers have separations \(r=2\) or \(r=3\), whereas coherence is minimized only at \(r=3\).
- For \(c_R<c<c_C\), resistance is maximized uniquely at \(r=2\), but coherence is minimized uniquely at \(r=3\).
- At \(c=c_C\), resistance is maximized only at \(r=2\), whereas both \(r=2\) and \(r=3\) minimize coherence.
- For \(c>c_C\), both criteria select separation \(r=2\).

Separation \(r=1\) is never optimal for either objective. Thus maximizing effective resistance does **not**, in general, solve noise-free two-leader coherence optimization even when all vertices have identical information centrality. The disagreement occupies a nonempty open interval of edge weights, not just one isolated example.

At the integer conductance \(c=4\), the resistance half-distances are
\[
 d_1=\frac{37}{1232},\quad d_2=\frac3{77},\quad d_3=\frac{13}{336},\qquad R_r=2d_r,
\]
while the three grounded traces are
\[
 C_1=\frac{5912}{25641},\quad C_2=\frac{3253}{16632},\quad C_3=\frac{584}{3003}.
\]
Therefore \(R_2>R_3\) by \(1/1848\), while \(C_2>C_3\) by \(241/216216\).

## Assumptions and scope
The graph has labeled vertices \(0,1,\ldots,5\), with edges between every pair of distinct vertices. For cyclic separation \(r=\min\{|i-j|,6-|i-j|\}\), assign conductance \(10\) for \(r=1\), \(1\) for \(r=2\), and \(c\) for \(r=3\). The Laplacian has \(L_{ij}=-w_{ij}\) for \(i\ne j\), and \(L_{ii}=\sum_{j\ne i} w_{ij}\). Every weight is positive for \(c>0\). The positive-definite grounded Laplacian is the principal submatrix obtained by deleting both leader rows and columns. The objective is its inverse trace, without the inessential factor \(1/2\) used for unit white-noise covariance. Effective resistance uses the full weighted Laplacian. The graph is vertex-transitive for every \(c>0\), so individual information centralities agree.

## Proof
**Spectral reduction.** The nonzero Laplacian eigenvalues, including multiplicities, are
\[
 \lambda_1=\lambda_5=13+2c,\qquad
 \lambda_2=\lambda_4=33,\qquad
 \lambda_3=40+2c.
\]
Set \(u=1/(13+2c)\), \(v=1/33\), and \(w=1/(40+2c)\). Let \(G=L^+\) and \(H=G^2\). By circulant symmetry let \(g_0=G_{ii}\), \(h_0=H_{ii}\), and for an unordered pair at separation \(r\), set
\[
 d_r=g_0-G_{ij}=R_r/2,\qquad e_r=h_0-H_{ij}.
\]
Fourier projection onto the eigenmodes yields
\[
\begin{array}{lll}
 d_1=(u+3v+2w)/6, & d_2=(u+v)/2, & d_3=(2u+w)/3,\\[2pt]
 e_1=(u^2+3v^2+2w^2)/6, & e_2=(u^2+v^2)/2, & e_3=(2u^2+w^2)/3.
\end{array}
\]

**Exact grounded-coherence identity.** For arbitrary connected vertex-transitive weighted graphs on \(N\) vertices, choose one leader \(i\) and write the one-vertex-grounded inverse as
\[
 B_{xy}=G_{xy}-G_{xi}-G_{iy}+g_0 \qquad(x,y\ne i).
\]
Grounding the second leader \(j\) is a Schur complement. Its trace is
\[
 C(\{i,j\})=\operatorname{tr}B-
 \frac{\sum_{x\ne i} B_{xj}^2}{B_{jj}}.
\]
Using \(\sum_xG_{xi}=0\), the equal diagonals of \(G\), and the corresponding equality for \(G^2\), gives
\[
 B_{jj}=2d_r,\qquad
 \sum_{x\ne i}B_{xj}^2=2e_r+N d_r^2,\qquad
 \operatorname{tr}B=\operatorname{tr}G+Ng_0.
\]
Thus, with \(N=6\), minimizing \(C_r\) is equivalent to maximizing
\[
 Q_r=\frac{e_r}{d_r}+3d_r,\qquad C_r=\operatorname{tr}G+6g_0-Q_r.
\]
This displays explicitly why resistance alone cannot determine the optimal pair: the squared-pseudoinverse contribution \(e_r/d_r\) is also present.

**Ordering all three separations.** Direct subtraction gives
\[
 d_2-d_1=\frac{u-w}{3}>0,
\]
and
\[
 Q_2-Q_1=
 \frac{(u-w)(u^2+6uv+4uw+v^2+4vw)}{(u+v)(u+3v+2w)}>0
\]
for every \(c>0\), because \(13+2c<40+2c\). Therefore separation one never maximizes resistance or minimizes coherence.

The remaining comparisons simplify to
\[
 d_2-d_3=\frac{2c^2+20c-103}{66(c+20)(2c+13)}
\]
and
\[
 Q_3-Q_2=
 -\frac{P(c)}{33(c+20)(c+23)(2c+13)(2c+31)}.
\]
The first numerator has precisely one positive zero \(c_R=-5+3\sqrt{34}/2\); it is negative before this zero and positive after. Moreover, \(P(0)<0\), \(P(4)<0<P(5)\), and
\[
 P'(c)=40c^3+1257c^2+9840c+4685>0 \qquad(c>0).
\]
Thus \(P\) has exactly one positive zero \(c_C\), with \(4<c_C<5\), and \(c_R<4<c_C\). These sign charts give the full claimed classification. At \(c=4\), exact substitutions in the preceding identities produce the displayed rational resistances and inverse traces.

## Verification
The accompanying `verify.py` uses exact symbolic arithmetic. It reconstructs both comparison rational functions and the strict inequalities from the spectral formulas, verifies the uniqueness-sign ingredients for the thresholds, and independently inverts the grounded Laplacians at six rational values of \(c\). For each value it checks three leader separations, all resistance half-distances, all biharmonic half-distances, the trace identity, and the sharp integer instance. Execute `python verify.py` with `sympy==1.14.0` installed. Those finite replays verify the claimed identities at selected parameters but are not a substitute for the symbolic proof of the continuum assertion.

## Relationship to prior work
Fitch and Leonard introduce joint centrality, including both resistance and biharmonic terms, for two noise-free leaders. Their explicit cycle and path solutions and their broad statement about choosing pairs at maximum resistance distance in equal-information-centrality networks motivate asking whether the latter shortcut holds on weighted vertex-transitive networks. The present exactly solved six-state example shows it need not: its resistance and coherence optimizers are different on a sharp open interval of conductances. This does not dispute their general joint-centrality formula, which correctly contains the extra term used in this proof. Lin, Fardad, and Jovanović give optimization algorithms and relaxations for leader selection, not this exact resistance-versus-coherence phase diagram. Clark, Bushnell, and Poovendran develop supermodular methods under link noise, a distinct optimization setting. These works motivate the objective and methods; none of the inspected portions yields the exact crossing identified here.

## Limitations
The phase diagram is for a specified one-parameter six-vertex positive weighted circulant. It does not classify general vertex-transitive graphs, all circulants, arbitrary numbers of leaders, or noisy leaders. The disagreement is strict on the stated open interval; no statement is made about other performance objectives. The correctness argument is exact but independent mathematical audit and exhaustive specialized-literature coverage have not been performed.

## References
1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first publicly posted 7 July 2014), especially Corollary 1, Section V-C, and Appendix A. https://arxiv.org/pdf/1407.1569
2. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first publicly posted 3 February 2013), Sections II and IV. https://arxiv.org/pdf/1302.0450
3. A. Clark, L. Bushnell, and R. Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, arXiv:1208.0946 (first publicly posted 4 August 2012), Sections I, II and IV. https://arxiv.org/pdf/1208.0946
