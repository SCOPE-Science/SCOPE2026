# A universal epoch-swap sign law for three-sequence neutral polymorphism

## Finding

For a sample of three neutral gene copies, interchanging two adjacent population-size epochs can make the expected counts of singleton and doubleton mutations move in **opposite directions**. The singleton direction is universal, while the doubleton direction has a sharp and complete phase diagram. The calculation is for the **unnormalized** expected site-frequency spectrum, rather than frequencies conditional on observing a polymorphic site.

Let the backward-time pair-coalescence hazards of the two intact blocks be \(u\) during length \(L_u\) and \(v\) during length \(L_v\), with \(0<u<v\) and both lengths positive. Compare the chronology \(u\) then \(v\), denoted \(uv\), to \(v\) then \(u\), denoted \(vu\). Let \(x\ge0\) be the accumulated pair-coalescence hazard before these blocks. Define

\[
X=e^{-uL_u},\quad Y=e^{-vL_v},\quad
D=\frac{v-u}{uv}(1-X)(1-Y)>0,\quad
R=\frac{(1+X+X^2)(1+Y+Y^2)}{3}.
\]

For \(j=1,2\), let \(\Delta_j=\mathbb E_{uv}[\xi_j]-\mathbb E_{vu}[\xi_j]\) be the change in expected numbers of mutations represented in precisely \(j\) sampled copies. Then

\[
\boxed{\Delta_1=\frac{3\mu D}{2}e^{-3x}(e^{2x}+R)>0,\qquad
\Delta_2=\frac{3\mu D}{2}e^{-3x}(e^{2x}-R).}
\]

Thus the doubleton change is negative, zero, or positive exactly according as \(R\) is greater than, equal to, or less than \(e^{2x}\). In particular, the total expected number of segregating sites always increases:

\[
\Delta_1+\Delta_2=3\mu D e^{-x}>0.
\]

The phase transition admits a universal formulation. Fix \(u<v\), positive lengths \(a,b\), and scale both block lengths as \(L_u=sa\), \(L_v=sb\), \(s>0\). Then \(R(s)\) strictly decreases from \(3\) to \(1/3\). If \(0\le x<\tfrac12\log 3\), there is exactly one positive \(s_*(x)\) defined by \(R(s_*)=e^{2x}\). Doubletons decrease for \(s<s_*\), tie for \(s=s_*\), and increase for \(s>s_*\). If \(x\ge\tfrac12\log3\), doubletons strictly increase for **every** positive scale. This cutoff is independent of the numerical hazards and of the length ratio.

## Assumptions and scope

The genealogy is Kingman's neutral coalescent of three contemporaneously sampled gene copies from a single panmictic population, with pair-coalescence hazard \(h(t)\ge0\) per unit of backward physical time. Mutations occur independently at a constant rate \(\mu>0\) per ancestral lineage and time unit, under the infinite-sites model with ancestral state ascertainable. The two models have the same measurable, locally integrable hazard before the swapped blocks and the same hazard afterward. The accumulated hazard \(x=\int_0^{t_0}h(t)\,dt\) is finite. On the blocks they have the indicated positive constants, with the whole blocks (including their lengths) transposed. The common tail is such that \(\int_0^\infty e^{-\int_0^t h(r)\,dr}\,dt<\infty\), guaranteeing finite expected total tree length; either history may be used for this condition. All parameters quantified above are otherwise arbitrary.

The sign assertion concerns expected absolute counts of derived singletons and doubletons over an idealized nonrecombining infinite-sites genomic segment. It is not an assertion about realized counts or about the normalized (conditional) site-frequency distribution.

## Proof

Write \(H(t)=\int_0^t h(r)\,dr\) and let \(K_t\) be the number of ancestral lineages at time \(t\). With three lineages, the initial total coalescence rate is \(3h(t)\); with two, it is \(h(t)\). By time change, the respective lineage-count probabilities are

\[
\Pr(K_t=3)=e^{-3H(t)},\qquad
\Pr(K_t=2)=\frac32\left(e^{-H(t)}-e^{-3H(t)}\right).
\]

At state \(K_t=3\), three branches lead to singleton descendants. At state \(K_t=2\), exactly one branch subtends one sample and the other subtends two. Hence the expected numbers of active singleton and doubleton branches are

\[
B_1(t)=3\Pr(K_t=3)+\Pr(K_t=2)
=\frac32(e^{-H(t)}+e^{-3H(t)}),
\quad
B_2(t)=\Pr(K_t=2)=\frac32(e^{-H(t)}-e^{-3H(t)}).
\]

Define the survival integrals \(J_\alpha=\int_0^\infty e^{-\alpha H(t)}\,dt\), for \(\alpha=1,3\). By the infinite-sites mutation assumption,

\[
\mathbb E[\xi_1]=\frac{3\mu}{2}(J_1+J_3),\qquad
\mathbb E[\xi_2]=\frac{3\mu}{2}(J_1-J_3).
\]

The histories agree before the swapped blocks. They also have the same cumulative hazard after the two blocks, namely \(x+uL_u+vL_v\), and the same subsequent hazard. Thus the prefix and tail cancel in both differences of \(J_\alpha\). On the two blocks, direct integration gives

\[
\begin{aligned}
F_\alpha(uv)&=\frac{1-e^{-\alpha uL_u}}{\alpha u}
+e^{-\alpha uL_u}\frac{1-e^{-\alpha vL_v}}{\alpha v},\\
F_\alpha(vu)&=\frac{1-e^{-\alpha vL_v}}{\alpha v}
+e^{-\alpha vL_v}\frac{1-e^{-\alpha uL_u}}{\alpha u}.
\end{aligned}
\]

Subtracting and restoring the prefix multiplier yields the exact **epoch-swap identity**

\[
J_\alpha(uv)-J_\alpha(vu)
=e^{-\alpha x}\frac{v-u}{\alpha uv}
(1-e^{-\alpha uL_u})(1-e^{-\alpha vL_v}).
\]

At \(\alpha=1\), this is \(e^{-x}D\). At \(\alpha=3\), the identities \(1-X^3=(1-X)(1+X+X^2)\) and \(1-Y^3=(1-Y)(1+Y+Y^2)\) make it \(e^{-3x}DR\). Substitution into the two branch-length formulas proves both boxed expressions and the strict singleton and total-count signs.

For the phase diagram, along a common duration scale \(s>0\), each factor \(1+e^{-us a}+e^{-2us a}\) and \(1+e^{-vs b}+e^{-2vs b}\) is strictly decreasing and continuous in \(s\). Their product divided by three therefore strictly decreases from \(3\) as \(s\downarrow0\) to \(1/3\) as \(s\to\infty\). The doubleton sign is the sign of \(e^{2x}-R(s)\), and \(e^{2x}\ge1\). A positive root exists precisely when \(e^{2x}<3\), is unique, and has the claimed order of signs. The boundary \(x=\tfrac12\log3\) remains strictly positive for every \(s>0\) because \(R(s)<3\).

Finally, for two sampled copies there is only the singleton class; its epoch-swap expected count changes by \(2\mu e^{-x}D>0\). Therefore three copies is the smallest sample in which singleton and doubleton changes can oppose each other.

## Verification

For an unequal-length witness, choose \(u=1\), \(v=2\), \(L_u=\log(4/3)\), and \(L_v=(\log2)/2\). Then \(X=3/4\), \(Y=1/2\), \(D=1/16\), and \(R=259/192\). With \(x=0\), the expected doubleton difference is strictly negative and the singleton difference strictly positive. With \(x=\log2\), both differences are strictly positive, because \(4>259/192\). The tails in these comparisons may be chosen to have constant hazard one.

The accompanying `checker.py` symbolically confirms four algebraic identities, compares both formulas with numerical quadrature on sixteen components for positive hazard profiles including unequal epoch lengths, verifies three bracketing instances of the unique duration threshold, and checks the exact rational witness. Run it with `python checker.py` using Python 3, SymPy, and mpmath. These finite checks are diagnostics; the quantified conclusions rely on the proof above.

## Relationship to prior work

The classical representation of the sample frequency spectrum by expected coalescent branch lengths is foundational. Polanski and Kimmel (2003) give general analytical formulas for variable-population SFS. Eriksson and collaborators (arXiv first posted November 30, 2009) develop distributions of total tree lengths under changing demography. Jenkins, Mueller and Song (2013) obtain broader triallelic formulas. Rosen, Bhaskar, Roch and Song (2018) give a geometric treatment of SFS images of piecewise-constant demographic histories.

Those general frameworks can compute the expected SFS for the present histories. The **claim assessed here** is not a new arbitrary-history representation but the stronger *explicit comparison*: a universal singleton sign under swapping intact demographic epochs, the exact opposing doubleton sign criterion, and the unique global cutoff along every duration-scaling ray. These particular comparison statements were not identified in the inspected results. A more general published rearrangement theorem could imply the comparison and remains a priority risk.

## Limitations

The result assumes a single neutral Kingman genealogy, no recombination or selection, perfectly known ancestral states, constant mutation intensity, and infinitely many nonrecurrent mutation sites. The universal cutoff pertains to an **absolute expected** spectrum of only three sampled copies, not the normalized spectrum, higher sample sizes, multilocus uncertainty, empirical demographic inference, or competing coalescent models. General variable-demography SFS formulas are established prior art. Independent historical-priority review has not been performed.

## References

1. A. Polanski and M. Kimmel (2003), *New Explicit Expressions for Relative Frequencies of Single-Nucleotide Polymorphisms With Application to Statistical Inference on Population Growth*, Genetics 165, 427–436. https://doi.org/10.1093/genetics/165.1.427
2. A. Eriksson, B. Mehlig, M. Rafajlovic and S. Sagitov (2009 preprint; first posted November 30, 2009), *Sample genealogies and genetic variation in populations of variable size*. https://arxiv.org/abs/0911.5672
3. P. A. Jenkins, J. W. Mueller and Y. S. Song (2013 preprint), *General triallelic frequency spectrum under demographic models with variable population size*. https://arxiv.org/abs/1310.3444
4. Z. Rosen, A. Bhaskar, S. Roch and Y. S. Song (2018), *Geometry of the Sample Frequency Spectrum and the Perils of Demographic Inference*, Genetics 210, 665–682. https://doi.org/10.1534/genetics.118.300733
