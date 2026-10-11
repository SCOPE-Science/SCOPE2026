# Review of A twelve-branch pressure certificate for the Minkowski correlation dimension

## Correctness

PASS. The primary source identifies \(D_2\) as the unique zero of the strictly increasing function
\[
P(s)=\log r(K_s).
\]
For \(s_0=0.847\), the included interval certificate proves uniformly on \([0,1]\) that the twelve-branch positive truncation sends
\[
g(x)=1+\frac{127}{120}x
\]
strictly above \(g+1/25000\). Positivity of all omitted branches gives the same lower bound for the full operator. Since \(g\le247/120\), this yields the exact pointwise subeigenfunction inequality
\[
K_{s_0}g\ge\left(1+\frac3{154375}\right)g.
\]
The resulting spectral-radius lower bound is standard and direct, so \(P(s_0)>0\) and \(D_2<s_0\). The Fourier exponent conclusion uses exactly the comparison proved by the source.

## Originality

PASS with a limited residual risk. The fresh source reports \(D_2/2=0.4223047\ldots\) as a numerical evaluation, but it does not provide an explicit rigorous decimal inequality obtained from a positive subeigenfunction or interval certificate. A numerical approximation alone does not imply the accepted strict bound.

Targeted searches for the exact source, pressure formulation, correlation dimension, certified value \(0.847\), and explicit Fourier-decay obstruction found no implication-equivalent result. Earlier inspected work concerns moments, Hausdorff dimension, regularity, or general Fourier/correlation principles rather than this finite pressure certificate.

## Value

PASS. The motivating source explicitly uses the correlation dimension to sharpen the known obstruction to Fourier decay, but its displayed \(0.4223047\ldots\) value is described as numerical. The accepted result turns that qualitative/numerical improvement into the proved, explicit inequality
\[
\eta_*<0.4235,
\]
which still strictly improves the older Hausdorff-dimension obstruction. The certificate is short, transparent, and replayable, so it provides a rigorous bridge from the abstract pressure characterization to a concrete Fourier-decay consequence.

Same-model review: passed. Independent audit: not yet performed.
