# Sharp temporal mode bound for variance of surviving-species richness

## Finding

Consider a community of \(n\ge1\) initially present species, all locally lost irreversibly at independent exponentially distributed extinction times. For every choice of strictly positive species-specific hazards \(\lambda_1,\ldots,\lambda_n\), let \(R(t)\) denote the number of species remaining at elapsed time \(t\). **The variance of surviving-species richness has at most \(n\) strict local maxima on positive time.**

The bound is attained for every size \(n\): the explicit hazards \(\lambda_j=20^{j-1}\), \(1\le j\le n\), make the variance exhibit exactly \(n\) distinct strict local maxima and exactly \(n-1\) strict local minima, in alternating order. In fact its derivative has exactly \(2n-1\) *simple* positive zeros. With arbitrary hazards, the derivative has at most \(2n-1\) positive zeros counted with multiplicity.

In particular, **two species already suffice for bimodality**, for hazards \((1,20)\). Meanwhile expected surviving richness decreases strictly at all times. The peak count can therefore grow without bound with community size even without correlated extinctions or colonization.

## Assumptions and scope

Fix an integer \(n\ge1\). Species \(j\) is present at time zero and has its irreversible extinction time \(T_j\), with \(T_j\sim\operatorname{Exp}(\lambda_j)\), \(\lambda_j>0\). The \(n\) random times are mutually independent. At any elapsed time \(t\ge0\), define
\[
R(t)=\sum_{j=1}^{n}\mathbf 1_{\{T_j>t\}},\quad
M(t)=\mathbb E[R(t)],\quad V(t)=\operatorname{Var}[R(t)].
\]
The derivatives and strict local extrema are with respect to real elapsed time \(t>0\). Equal extinction rates are allowed in the universal upper bound; the sharp construction uses pairwise distinct rates. No species reappears, and no interactions or shared environmental shocks occur.

Independence gives, exactly,
\[
M(t)=\sum_{j=1}^n e^{-\lambda_j t},\qquad
V(t)=\sum_{j=1}^n e^{-\lambda_j t}(1-e^{-\lambda_j t}).
\]
Thus \(M'(t)=-\sum_j\lambda_j e^{-\lambda_j t}<0\) for all \(t\ge0\).

## Proof

**1. Universal upper bound.** Differentiation yields
\[
V'(t)=\sum_{j=1}^{n}\lambda_j(2e^{-2\lambda_jt}-e^{-\lambda_jt}). \tag{1}
\]
After merging coincident exponents, this is a nonzero linear combination of at most \(2n\) exponential functions with pairwise distinct real exponents; it is nonzero because \(V'(0)=\sum_j\lambda_j>0\).

We recall and prove the classical exponential zero-count fact. A nonzero function of the form \(F(t)=\sum_{i=1}^{m}c_ie^{-a_it}\), with distinct real \(a_i\), has at most \(m-1\) real zeros on any interval, counted with their multiplicities. For \(m=1\) this is immediate. Order \(a_1<\cdots<a_m\), and multiply by \(e^{a_1t}\). The derivative of the resulting function is a combination of at most \(m-1\) distinct exponential functions. If the multiplied function has \(k\) zeros counted with multiplicity, its derivative has at least \(k-1\) such zeros, by Rolle's theorem between distinct zeros and the standard multiplicity decrement at repeated zeros. Inductively \(k-1\le m-2\), whence \(k\le m-1\). A nonzero constant multiplier and exponential factor never alter zeros.

Applying this fact to (1), \(V'\) has at most \(2n-1\) positive zeros, multiplicities included. If a continuously differentiable function has \(s\) distinct strict local maxima in an interval, it has at least \(s-1\) distinct intervening local minima, and all \(2s-1\) locations are stationary. Here \(V\) is analytic; consequently \(2s-1\le2n-1\) and \(s\le n\).

**2. Explicit sharpness and strictly alternating signs.** For every \(n\), set \(\lambda_j=20^{j-1}\). Define
\[
f(z)=2e^{-2z}-e^{-z},\quad z\ge0.
\]
Writing \(u=e^{-z}\in(0,1]\), we have \(f(z)=2u^2-u\), hence \(f(z)\ge-1/8\), with equality exactly at \(z=\log4\). Furthermore \(f(z)>0\) on \(0\le z<\log2\), and for positive \(z\), \(f(z)>-e^{-z}\). Equation (1) is \(V'(t)=\sum_j\lambda_j f(\lambda_jt)\).

For every \(j=1,\ldots,n\), introduce a *negative* witness
\[
a_j=\frac{\log4}{\lambda_j}.
\]
The \(j\)-th term of \(V'(a_j)\) equals \(-\lambda_j/8\). All terms with index \(i>j\) are strictly negative, because their arguments exceed \(\log2\). Each earlier term is at most \(\lambda_i\), and
\[
\sum_{i<j}\lambda_i < \frac{\lambda_j}{19}<\frac{\lambda_j}{8}.
\]
Therefore \(V'(a_j)<0\) for every \(j\).

For every \(j=1,\ldots,n-1\), also introduce a *positive* witness
\[
b_j=\frac{\log2}{2\lambda_j}.
\]
The \(j\)-th term is \(\lambda_j(1-1/\sqrt2)>\lambda_j/4\). Every earlier term is positive, since its argument is below \(\log2\). The combined negative contributions of all later terms have absolute value less than
\[
\lambda_j\sum_{k=1}^{\infty}20^k2^{-10\cdot20^{k-1}}
<\lambda_j\frac{40}{1024}<\frac{\lambda_j}{20}.
\]
For the first strict bound, the first term equals \(20/1024\); each successive term is less than half its predecessor because their ratio is \(20\cdot2^{-190\cdot20^{k-1}}<1/2\). Thus \(V'(b_j)>0\).

Finally, the positive witnesses occur in the strict order
\[
0<a_n<b_{n-1}<a_{n-1}<b_{n-2}<\cdots<b_1<a_1.
\]
The displayed inequalities follow by substituting the common ratio \(20\); equivalently, for consecutive scales the positive-time multiples of \(\log2/\lambda_j\) are \(2,10,40\). Together with \(V'(0)>0\), the signs at this ordered list alternate exactly \(+,-,+,-,\ldots,+,-\). The intermediate value theorem therefore supplies at least \(2n-1\) **distinct** positive zeros of \(V'\), each separating opposite derivative signs. By the zero-count bound these are all the zeros and all have multiplicity one.

The successive sign changes consequently give exactly \(n\) strict, nondegenerate local maxima and exactly \(n-1\) strict, nondegenerate local minima. For \(n=1\), the same reasoning uses only the signs at \(t=0\) and \(a_1\). This proves both sharp assertions for all \(n\).

**3. Structural stability.** Because all constructed derivative zeros are simple and separated, each persists under sufficiently small perturbations of all positive hazards by the implicit function theorem. The upper bound forbids additional maxima. Hence the \(n\)-peak behavior occupies a nonempty open neighborhood of the displayed hazard vector, not just an isolated choice of parameters.

## Verification

The standalone `verify.py` evaluates equation (1) directly for \(1\le n\le10\), using the witness times above and all \(110\) predicted alternating derivative signs, and checks key rational bounds. It completed successfully. These calculations test instances and guard against transcription/sign mistakes; **they do not prove the unbounded-in-\(n\) assertion**, which follows exclusively from the zero-count induction and uniform witness inequalities above. No population simulation or sampling approximation is used in the proof.

To reproduce, run `python verify.py` with Python 3 and its standard library. For all \(n\), the exact rate vector and all witnesses are specified by the displayed formulas.

## Relationship to prior work

The classical Chebyshev property of exponentials provides the zero-count argument; that general analytic fact is not claimed as original. Prior ecological research examines heterogeneity in population persistence and dynamic species abundance distributions. Fox and Kendall (2002) study demographic heterogeneity and variance reduction; Engen (2007) studies heterogeneous species-extinction dynamics; Sæther, Engen and Grøtan (2013) provide a full-text synthesis of variable community richness and species-abundance distributions; Drake (2014) studies experimental extinction-time tails and questions whether exponential tails hold empirically.

The narrowly assessed new contribution is the **sharp all-community-size temporal mode count for the variance of independent exponentially surviving species, together with the explicit all-size attainment and its robustness**. The inspected full texts of the 2013 synthesis and 2014 experimental article analyze different uncertainty statistics and do not state this exact extremum classification. The potentially relevant Engen (2007) article was identifiable but its full text could not be retrieved; no assertion of its whole-document noncoverage is made. Search results and abstracts alone are not proofs of priority.

## Limitations

This is a conditional mathematical theorem. Real extinctions are often correlated, have age-dependent hazards, include colonization, and show nonexponential persistence-time tails. In such settings neither the zero-count upper bound nor the construction is asserted. The very large rate separations used to attain all \(n\) peaks are mathematically explicit and robust to sufficiently small perturbations but need not be plausible in any specific ecological community. The result concerns variation *between independently repeated hypothetical communities*, not the variance of one observed richness time series along a single path. It does not identify the optimal community configuration under external biological constraints. Bibliographic originality remains subject to independent scholarly review.

## References

- Fox, G. A. and Kendall, B. E. (2002), *Demographic Stochasticity and the Variance Reduction Effect*, Ecology 83(7), 1928-1934. https://doi.org/10.2307/3071775
- Engen, S. (2007), *Heterogeneity in dynamic species abundance models: the selective effect of extinction processes*, Mathematical Biosciences 210, 490-507. https://doi.org/10.1016/j.mbs.2007.06.002
- Sæther, B.-E., Engen, S., and Grøtan, V. (2013), *Species diversity and community similarity in fluctuating environments: parametric approaches using species abundance distributions*, Journal of Animal Ecology 82, 721-738. First online publication 11 April 2013. https://doi.org/10.1111/1365-2656.12068
- Drake, J. M. (2014), *Tail probabilities of extinction time in a large number of experimental populations*, Ecology 95, 1119-1126. First online publication 1 May 2014. https://doi.org/10.1890/13-1107.1
