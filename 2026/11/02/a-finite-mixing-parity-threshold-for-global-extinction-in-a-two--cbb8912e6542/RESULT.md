# A finite-mixing parity threshold for global extinction in a two-patch saturation model

## Finding

Consider two equally sized epidemiological patches. At every slow time step, individuals perform exactly \(k\geq1\) fast symmetric migration rounds, followed by one local, saturation-limited infection update. Migration in one round has exchange fraction \(p\in(1/2,1)\). The patch infection levels \(x=(x_1,x_2)\in[0,1]^2\) evolve by
\[
 x_i(t+1)=\frac{r_i (P^k x(t))_i}{1+a_i(P^k x(t))_i},\qquad
 P=\begin{pmatrix}1-p&p\\p&1-p\end{pmatrix},\quad i=1,2,
\]
where \(r_1,r_2,a_1,a_2>0\) and \(a_i\geq r_i-1\). The latter condition makes the epidemiological square forward invariant. This rational infection map is a specific phenomenological saturation law; it is **not** the four-compartment SEIRS map of the motivating paper.

Suppose the isolated patch multipliers satisfy the mixed source–sink condition
\[
 r_1r_2<1<\bar r:=\frac{r_1+r_2}{2}.
\]
Put
\[
 \mu=2p-1\in(0,1),\qquad
 \tau=\frac{\bar r-1}{\bar r-r_1r_2}\in(0,1).
\]
**Theorem (sharp finite-mixing parity dichotomy).** For every admissible choice above and every integer \(k\geq1\):

1. If \(k\) is even, there is exactly one positive equilibrium, and it attracts every trajectory with a nonzero initial infection state.
2. If \(k\) is odd and \(\mu^k<\tau\), the same globally attracting positive equilibrium exists.
3. If \(k\) is odd and \(\mu^k\geq\tau\), the disease-free state is globally attracting on \([0,1]^2\) and no positive equilibrium exists. **Equality belongs to extinction.**

The finite-mixing invasion multiplier has the closed form
\[
 \Lambda_k=\frac{\bar r(1+s_k)+\sqrt{\bar r^2(1+s_k)^2-4r_1r_2s_k}}{2},
 \qquad s_k=(1-2p)^k.
\]
It increases strictly as a function of \(s_k\), and the unique crossing of \(1\) is at \(s_k=-\tau\). Thus all even numbers of migration rounds are endemic, whereas an initial finite set of odd numbers may eradicate infection **even though the infinite-fast-mixing limit is endemic**. For odd integers, extinction occurs exactly for
\[
 k\leq \frac{\log\tau}{\log\mu}.
\]
This is a statement about changing the number of movement episodes *within each slow step*, not alternating disease parameters across successive slow steps.

For example, take \(r_1=2\), \(r_2=1/5\), \(p=9/10\), and \(a_i=r_i\). Then \(\bar r=11/10\), \(r_1r_2=2/5\), \(\mu=4/5\), and \(\tau=1/7\). Exactly \(k\in\{1,3,5,7\}\) yields global extinction, whereas every even \(k\) and every odd \(k\geq9\) yields a globally attracting positive equilibrium. At \(k=1\), \(\Lambda_1=0.6862811814\ldots\); at \(k=9\), \(\Lambda_9=1.0057411255\ldots\); and as \(k\to\infty\), \(\Lambda_k\to11/10>1\).

## Assumptions and scope

The population sizes are equal and unchanged by symmetric migration; an infection level is the fraction infected in a patch after the slow update. Movement acts identically on infected and uninfected individuals, so \(P\) averages the infection fractions. The two local infection maps are increasing and strictly concave, and their slopes at zero are \(r_i\). The parameters \(a_i>0\) allow arbitrary saturation strengths subject only to invariance of the state square. All results concern the deterministic discrete-time map, with no migration while the local update takes place. For positive mixing \(0<p<1\), the matrix \(P^k\) is strictly positive.

The source–sink regime imposes \(r_1r_2<1<\bar r\), which entails (up to relabeling) \(r_1>1>r_2\). No conclusions about finite-population stochastic extinction times, exposed or recovered compartments, unequal patch sizes, or a nonconstant migration policy are claimed.

## Proof

**1. Spectral formula and parity.** Write \(D=\operatorname{diag}(r_1,r_2)\), \(q=r_1r_2\), and \(s=(1-2p)^k\). Diagonalizing the symmetric two-patch migration matrix gives exactly
\[
 P^k=\frac12\begin{pmatrix}1+s&1-s\\1-s&1+s\end{pmatrix}.
\]
The disease-free Jacobian \(M_k=DP^k\) is strictly positive. Its trace and determinant are
\[
 \operatorname{tr} M_k=\bar r(1+s),\qquad \det M_k=qs.
\]
The displayed formula for \(\Lambda_k\) follows by the quadratic formula; its positive square root is real because \(M_k\) is strictly positive and has two real eigenvalues. Equivalently, the discriminant is \(\frac14(r_1-r_2)^2(1+s)^2+ r_1r_2(1-s)^2\), up to the same conventional normalization; directly it equals \(\bigl((r_1-r_2)(1+s)/2\bigr)^2+r_1r_2(1-s)^2>0\).

**2. Strict dependence on residual mixing.** For \(-1<s<1\), differentiate the characteristic equation
\[
 \Lambda^2-\bar r(1+s)\Lambda+qs=0
\]
to obtain
\[
 \frac{d\Lambda}{ds}=\frac{\bar r\Lambda-q}{\sqrt{\bar r^2(1+s)^2-4qs}}.
\]
Here \(r_1\ne r_2\) since \(q<1<\bar r\). At \(s=-1\), the numerator is \(\sqrt q(\bar r-\sqrt q)>0\) by strict arithmetic–geometric mean inequality. It cannot vanish at an interior \(s\): if \(\Lambda=q/\bar r\), substitution in the characteristic equation would force \(\Lambda=\bar r\), contradicting \(q<\bar r^2\). Continuity proves strict positivity throughout. The boundary values are \(\Lambda(-1)=\sqrt q<1\), \(\Lambda(0)=\bar r>1\), and \(\Lambda(1)=\max\{r_1,r_2\}\). Inserting \(\Lambda=1\) into the characteristic polynomial yields its unique crossing
\[
 s_*=-\frac{\bar r-1}{\bar r-q}=-\tau,
\]
with \(0<\tau<1\), because \(q<1<\bar r\). Since \(s=(-\mu)^k\), every even \(k\) has \(s>0\) and is supercritical, and odd \(k\) is subcritical or critical precisely when \(\mu^k\geq\tau\). Taking logarithms proves the integer cutoff.

**3. Global consequences, including equality.** Let \(F_k:[0,1]^2\to[0,1]^2\) denote the nonlinear update, and let \(B=P^k\). Since \(B\) is positive, \(F_k\) is strictly order preserving for nonidentical ordered inputs and sends every nonzero input into the strictly positive interior. Componentwise,
\[
 0\leq F_k(x)_i=\frac{(M_kx)_i}{1+a_i(Bx)_i}\leq(M_kx)_i,
\]
with strict inequality for every component whenever \(x\ne0\). If \(\Lambda_k<1\), iterating gives \(F_k^t(x)\leq M_k^t x\to0\). If \(\Lambda_k=1\), a positive left Perron vector \(\ell\) gives the strict Lyapunov descent \(\ell^\top F_k(x)<\ell^\top x\) for every nonzero \(x\). Since the state square is compact, no nonzero omega-limit point is possible: otherwise the decrement would have a positive minimum on an invariant compact subset separated from zero. Hence every trajectory converges to zero also at equality.

If \(\Lambda_k>1\), take the positive right Perron vector \(v\) and a sufficiently small \(\varepsilon>0\) so that \(F_k(\varepsilon v)\geq\varepsilon v\), with strict inequalities. The all-ones vector satisfies \(F_k(\mathbf1)\leq\mathbf1\) by \(a_i\geq r_i-1\). Order-preserving iteration from these lower and upper solutions gives positive fixed points between them. They coincide: if two positive fixed points \(x,y\) differ, choose one orientation with \(c=\max_i x_i/y_i>1\). Then \(x\leq cy\), with equality in at least one coordinate, but the strictly subhomogeneous law
\[
 F_k(cy)_i=\frac{c(M_ky)_i}{1+c a_i(By)_i}<cF_k(y)_i
\]
contradicts \(x=F_k(x)\leq F_k(cy)<cy\) at that coordinate. This proves uniqueness. Any nonzero initial state becomes positive after one step; it can then be sandwiched between a sufficiently small multiple of \(v\) and \(\mathbf1\). The monotone lower and upper iterates both converge to the unique positive fixed point, so every nonzero trajectory does also. This completes all cases.

## Verification

The standalone script \(\texttt{verification/check\_parity.py}\) uses exact rational arithmetic to check the migration power identity and characteristic coefficients at \(68\) combinations of rational migration fractions and integers \(1\le k\le17\). It independently evaluates the eigenvalue formula, threshold, and nonlinear iterates for the explicit \((2,1/5,9/10)\) example, including the equality case at \(k=1\), \(p=4/7\). On a representative initial infection state, \(30000\) iterations converge toward extinction for \(k=1,3,5,7\) and toward strictly positive steady states for \(k=2,4,6,8,9,10,11\). These checks support, but do not replace, the proof for all parameters and integers. The proof of global attraction is fully analytic.

## Relationship to prior work

Bravo de la Parra and Sanz-Lorenzo (2021, Sect. 3–5) provide the sequential fast-movement/slow-epidemic framework \(\mathcal S\circ\mathcal F^{(k)}\), and demonstrate large-\(k\) reduction for a different four-compartment SEIRS map. Their Theorem 6 and Corollary 9 concern sufficiently large \(k\) and do not give the present exact finite-\(k\) parity threshold or global positive attractor for the two-dimensional saturating update.

Grumbach and collaborators (2023) analyze related symmetric two-patch Beverton–Holt population maps, including high exchange fractions, but their main classification assumes both isolated patches are sources \(r_i>1\) and concerns the equilibrium total population as dispersal varies. Its growth-before-dispersal model with a single movement step does not state the present source–sink, arbitrary-number-of-movement-rounds extinction/endemic alternation. The existence of classical Perron thresholds and general monotone concave map theory is not claimed as new. The contribution is their exact coupling into an all-integer, nonlinear global parity phase diagram, with a finite eradication window that is reversed by further mixing.

The continuous-time patch models of Salmani and van den Driessche (2006), Bichara and collaborators (2015), and Das and Stolerman (2024) analyze migration-dependent epidemic thresholds, but their flow or residence-time formulations do not encode \(P^k\) with a negative migration eigenvalue that changes sign under parity. Searches did not establish an exact equivalent result for this sequential map; mathematical equivalence outside the inspected sources remains a residual risk.

## Limitations

This is a deterministic two-patch theorem for a specified rational saturating law, not a result about the full SEIRS equations of the motivating paper. The term 'extinction' denotes convergence to zero, not finite-time elimination. The local gains \(r_i\) need not equal the conventional next-generation \(R_0\) of a multistage SEIRS model. Strong exchange \(p>1/2\) is essential; continuous-time symmetric mixing is not represented by negative subdominant eigenvalues. Nothing here proves a parity effect in the SEIRS model without a separate analysis. The originality assessment is based on inspected accessible sources, not a proof that the result is absent from all literature.

## References

- R. Bravo de la Parra and L. Sanz-Lorenzo, *Discrete epidemic models with two time scales*, Advances in Difference Equations 2021, article 478, publicly published 2021-10-30. DOI: https://doi.org/10.1186/s13662-021-03633-0. Open full text also at https://pmc.ncbi.nlm.nih.gov/articles/PMC8556850/.
- C. Grumbach, F. N. Reurik, J. Segura, D. Franco, and F. M. Hilker, *The effect of dispersal on asymptotic total population size in discrete- and continuous-time two-patch models*, Journal of Mathematical Biology 87 (2023), article 60. DOI: https://doi.org/10.1007/s00285-023-01984-8.
- M. Salmani and P. van den Driessche, *A model for disease transmission in a patchy environment*, Discrete and Continuous Dynamical Systems B 6 (2006), 185–202. DOI: https://doi.org/10.3934/dcdsb.2006.6.185.
- D. Bichara, Y. Kang, C. Castillo-Chavez, R. Horan, and C. Perrings, *SIS and SIR epidemic models under virtual dispersal*, arXiv:1503.08881 (2015). https://arxiv.org/abs/1503.08881.
- H. K. Das and L. M. Stolerman, *Epidemic Thresholds and Disease Dynamics in Metapopulations: The Role of Network Structure and Human Mobility*, SIAM J. Applied Dynamical Systems 23 (2024), 1579–1609. DOI: https://doi.org/10.1137/23M1579522.
