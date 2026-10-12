# The price-metric variance law for fastest mixing on weighted birth-death paths

## Finding

**Theorem (complete heterogeneous-price, heterogeneous-mass path design).** Fix an integer \(n\ge 2\), positive stationary masses \(\pi_1,\ldots,\pi_n\) with \(\sum_{j=1}^n\pi_j=1\), and positive edge prices \(c_1,\ldots,c_{n-1}\). For \(1\le i<n\), a nonnegative conductance \(w_i\) on the edge \(\{i,i+1\}\) costs \(c_iw_i\). Under the unit budget \(\sum_i c_iw_i=1\), maximize the smallest positive eigenvalue \(\gamma(w)\) of the reversible birth-death generator \(-\operatorname{diag}(\pi)^{-1}L(w)\), where \(L(w)\) is the conductance-weighted path Laplacian.

Set \(g_i=\sqrt{c_i}\), \(s_1=0\), \(s_j=\sum_{r=1}^{j-1}g_r\) for \(2\le j\le n\), and \(\mu=\sum_j\pi_js_j\). Define the strictly positive weighted variance
\[
D=\sum_{j=1}^n\pi_j(s_j-\mu)^2
 =\sum_{1\le a<b\le n}\pi_a\pi_b\left(\sum_{r=a}^{b-1}\sqrt{c_r}\right)^2.
\]
For each edge define the strictly positive left-side flux
\[
F_i=\sum_{j=1}^i\pi_j(\mu-s_j)
=\sum_{a\le i<b}\pi_a\pi_b(s_b-s_a).
\]
Then the globally optimal spectral gap and **unique** maximizing conductances are
\[
\boxed{\gamma^*=\frac1D,\qquad w_i^*=\frac{F_i}{D\sqrt{c_i}}\quad(1\le i<n).}
\]
Every optimal edge conductance is strictly positive; the optimal spectral-gap eigenfunction is uniquely proportional to \(j\mapsto s_j-\mu\), and the optimal spectral gap is simple. All optimal conductances and the gap are computable in \(O(n)\) arithmetic operations and square roots. For each \(i\), their price sensitivity satisfies \(\partial\gamma^*/\partial c_i=-\gamma^*w_i^*\), with the stationary masses held fixed.

## Assumptions and scope

The state set is the ordered path \(\{1,\ldots,n\}\). For an edge-rate vector \(w\), the generator has \(Q_{i,i+1}=w_i/\pi_i\), \(Q_{i+1,i}=w_i/\pi_{i+1}\), \(Q_{ij}=0\) for other distinct states, and diagonal entries chosen so that every row sums to zero. Detailed balance with \(\pi\) follows from \(\pi_iQ_{i,i+1}=w_i=\pi_{i+1}Q_{i+1,i}\). The eigenvalue \(\gamma(w)\) is the \(L^2(\pi)\) exponential convergence rate, not the mixing time in total variation and not the discrete-time second-largest-eigenvalue-modulus objective. At a disconnected boundary allocation \(w_i=0\) for some edge, define \(\gamma(w)=0\); such allocations cannot maximize the positive optimum.

For every nonconstant real vector \(f\), with \(\bar f=\sum_j\pi_j f_j\),
\[
\gamma(w)=\inf_{f\not\equiv\text{constant}}
\frac{\sum_{i=1}^{n-1}w_i(f_{i+1}-f_i)^2}
     {\sum_{j=1}^n\pi_j(f_j-\bar f)^2}.
\]
The normalization \(\sum\pi_j=1\) is essential: it fixes the generator scale and budget interpretation. If unnormalized positive vertex masses are used instead, normalize them first and adjust the generator to that convention.

## Proof

**1. The path covariance kernel.** Put \(P_i=\sum_{j=1}^i\pi_j\) for \(1\le i<n\) and introduce the symmetric \((n-1)\)-by-\((n-1)\) matrix
\[
G_{ij}=P_{\min(i,j)}\bigl(1-P_{\max(i,j)}\bigr).
\]
Every entry is strictly positive, because all stationary masses are positive and both sides of every edge are nonempty. For any \(f\), write \(d_i=f_{i+1}-f_i\). Since \(f_j=f_1+\sum_{i<j}d_i\), the variance-covariance formula for the nested indicators \(\boldsymbol1_{\{J>i\}}\), where \(\Pr(J=j)=\pi_j\), proves the exact identity
\[
\sum_{j=1}^n\pi_j(f_j-\bar f)^2
       =\sum_{i,r=1}^{n-1}G_{ir}d_id_r=d^{\mathsf T}Gd.
\]
In particular \(D=g^{\mathsf T}Gg\). A direct expansion using the same indicators shows \((Gg)_i=\sum_{a\le i<b}\pi_a\pi_b(s_b-s_a)=F_i>0\).

**2. A universal upper certificate.** Insert the strictly increasing test vector \(f=s\) into the variational formula. For every feasible \(w\), its Dirichlet numerator is exactly \(\sum_iw_ig_i^2=\sum_i c_iw_i=1\), while its \(\pi\)-variance is \(D\). Thus \(\gamma(w)\le1/D\) for every feasible allocation, including boundary allocations.

**3. Feasibility and an exact all-vector lower certificate.** Define \(\widehat w_i=(Gg)_i/(Dg_i)\). These numbers are strictly positive and
\[
\sum_i c_i\widehat w_i
 =\frac1D\sum_i g_i(Gg)_i
 =\frac{g^{\mathsf T}Gg}{D}=1.
\]
For an arbitrary vector \(f\) and its edge differences \(d_i\), direct symmetric expansion gives the **exact square identity**
\[
\begin{aligned}
&\sum_i\widehat w_i d_i^2-\frac1D d^{\mathsf T}Gd\\
&\qquad=\frac{1}{2D}\sum_{i,r=1}^{n-1}
 G_{ir}g_ig_r\left(\frac{d_i}{g_i}-\frac{d_r}{g_r}\right)^2\ge0.
\end{aligned}
\]
Hence \(\gamma(\widehat w)\ge1/D\). Testing \(f=s\) again gives equality, proving global optimality and the claimed optimal gap. Because every \(G_{ir}>0\), equality in this square identity requires \(d_i/g_i\) to be the same for every edge; the optimal nonconstant eigenspace is therefore one-dimensional. When \(n=2\) it is automatically one-dimensional.

**4. Global uniqueness.** Suppose a different feasible allocation \(w\) attains \(\gamma(w)=1/D\). The Rayleigh quotient of the fixed nonconstant vector \(s\) still equals \(1/D\), so \(s-\mu\boldsymbol1\) is a minimizing generalized eigenvector and satisfies \(L(w)s=D^{-1}\operatorname{diag}(\pi)(s-\mu\boldsymbol1)\). Summing its first \(i\) vertex equations telescopes the edge fluxes:
\[
-w_ig_i=\frac1D\sum_{j=1}^{i}\pi_j(s_j-\mu),
\qquad\text{hence}\qquad w_i=\frac{F_i}{Dg_i}.
\]
Thus all \(w_i\) coincide with \(\widehat w_i\). No other feasible allocation is optimal, including disconnected boundary allocations.

**5. Sensitivity and computational complexity.** Since \(D=g^{\mathsf T}Gg\) with \(G\) independent of prices, differentiation with respect to \(c_i=g_i^2\) yields \(\partial D/\partial c_i=(Gg)_i/g_i=Dw_i^*\). Differentiating \(\gamma^*=D^{-1}\) gives \(\partial\gamma^*/\partial c_i=-\gamma^*w_i^*\). A forward scan computes the cumulative positions, \(\mu\), and \(D\); a second scan computes every \(F_i\). This proves the stated linear-time construction without constructing \(G\).

## Verification

The standalone, dependency-free program `verify.py` uses exact rational arithmetic for positive rational masses and square prices (making all \(g_i\) rational). It checks weighted centering, exact variance, budget feasibility, the generalized eigenrelation, and eight exact signed edge-gradient tests of the sum-of-squares identity on each instance. With its fixed random seed it returns:

`VERIFY_OK 801 exact positive-mass/price instances; 6408 exact ground-state quadratic-identity checks; budgets/eigenrelations`

An additional numerical stress test, run independently of the standalone checker with non-square positive real prices, compared the closed-form gap against the second generalized Laplacian eigenvalue for 420 instances on paths of \(2\) through \(15\) vertices; the maximum observed relative discrepancy was \(2.36\times10^{-14}\). Neither finite test is used as proof of the quantified theorem; Steps 1–5 establish it for every allowed real parameter.

For the concrete four-state example \(\pi=(1,2,3,4)/10\) and \(c=(1,4,9)\), one has \(s=(0,1,3,6)\), \(\mu=7/2\), \(D=101/20\), and
\[
\gamma^*=\frac{20}{101},\qquad
(w_1^*,w_2^*,w_3^*)=\left(\frac7{101},\frac{17}{202},\frac{20}{303}\right).
\]
The exact budget check reads \(7/101+4(17/202)+9(20/303)=1\). For uniform stationary masses and unit prices, the theorem specializes to \(\gamma^*=12/(n^2-1)\) and \(w_i^*=6i(n-i)/[n(n^2-1)]\) under the stated generator normalization.

## Relationship to prior work

Fiedler's 1990 absolute-algebraic-connectivity theorem and its interpretation in Göring, Helmberg, and Wappler's 2005 preprint address maximizing the ordinary weighted graph Laplacian's second eigenvalue under a **uniform** edge-weight budget. Their tree case includes the unit-mass, unit-price specialization after normalization, and the later embedding interpretation is a conceptual antecedent of the path-position certificate used here. The present theorem fixes **arbitrary positive stationary vertex masses together with individually varying positive linear edge prices** and determines the normalized continuous-time generator's unique optimum explicitly; the uniform-mass uniform-price results alone do not give these formulas.

Wan and collaborators' 2008 tree-design theorem provides a more general-tree algorithm for the uniform-mass and uniform-price optimization model. Shafi, Arcak, and El Ghaoui's 2010 paper develops graph node-and-edge weighting through spectral semidefinite constraints and demonstrates a numerical chain example under a different eigenvalue-ratio objective. These broader frameworks provide numerical formulations, but their inspected statements do not give the present all-parameter square-root-price variance formula, linear-time rates, or exact flux certificate. Boyd, Diaconis, Sun, and Xiao's 2006 path theorem optimizes a discrete-time symmetric stochastic matrix under row-probability constraints; its \(\cos(\pi/n)\) SLEM is a different objective and normalization. Richter and Rocha's 2014 preprint gives formulas for unpriced double-broom graph families and algorithmic results for uniform-weight tree optimization.

## Limitations

The theorem does not cover graphs with cycles or branching paths, prices or stationary masses equal to zero, maximum individual jump-rate constraints, discrete-time fastest mixing, total-variation mixing times, or nonreversible generators. The unit-budget and normalized-stationary-mass conventions cannot be dropped without rescaling. Optimality and uniqueness are proved internally, but no independent audit or external mathematical validation has been performed. Historical originality remains uncertain because the complete text of Fiedler's 1990 article could not be inspected; analogous weighted-mass versions might be present in less accessible literature. A general graph semidefinite formulation can of course represent this path problem, without itself providing the theorem's explicit optimal rates.

## References

1. M. Fiedler, *Absolute algebraic connectivity of trees*, Linear and Multilinear Algebra **26** (1990), 85–106. DOI: https://doi.org/10.1080/03081089008817967 (abstract available; full text not inspected).
2. F. Göring, C. Helmberg, and M. Wappler, *Embedded in the Shadow of the Separator*, Optimization Online public preprint dated **2005-09-02**, https://optimization-online.org/2005/09/1202/ ; full preprint https://optimization-online.org/wp-content/uploads/2005/09/1202.pdf .
3. Y. Wan, S. Roy, X. Wang, A. Saberi, T. Yang, M. Xue, and B. Malek, *On the structure of graph edge designs that optimize the algebraic connectivity*, CDC 2008, 805–810, DOI: https://doi.org/10.1109/CDC.2008.4738734 .
4. S. Y. Shafi, M. Arcak, and L. El Ghaoui, *Designing Node and Edge Weights of a Graph to Meet Laplacian Eigenvalue Constraints*, Allerton 2010, DOI: https://doi.org/10.1109/ALLERTON.2010.5707021 .
5. S. Boyd, P. Diaconis, J. Sun, and L. Xiao, *Fastest Mixing Markov Chain on a Path*, American Mathematical Monthly **113** (2006), 70–74, https://web.stanford.edu/~boyd/papers/fmmc_path.html .
6. S. Richter and I. Rocha, *Absolute Algebraic Connectivity of Double Brooms*, open 2014 manuscript, https://www.tu-chemnitz.de/mathematik/preprint/2014/PREPRINT_10.pdf .
