# Independent mathematical audit

## correctness

PASS

After conditioning on each column being nonempty, the independent column states 10, 01 and 11 have probabilities t,t,u. Coverage of the left vertices removes exactly the two single-row configurations of mass h each. The edge means and joint probabilities then give v,a,b,c as stated. Independently, the symmetric coordinate is (1+1_{11})/sqrt(2) and the antisymmetric coordinate is (X_1-X_2)/sqrt(2); their cross-block covariance vanishes by row swap. The symmetric block has diagonal u(t-h)/z^2 and off-diagonal -h u^2/z^2; the antisymmetric block has diagonal (t-h)/z and off-diagonal -h/z. This gives the four claimed eigenvalues; A>0 since nt^(n-1)<1 for all n>=2, and B>A. The inverse blocks have off-diagonals zh/(tB) and zh/(tA), respectively. Transforming back gives q_c as half their difference, q_b as half their sum, q_a=z/u+q_c, and the stated q_0. For q_a the numerator AB-(n-1)uh^2=A^2+(n-1)h(2tA-uh) is strictly positive: the factor t^(n-2)(1+2(n-1)t) in (2tA-uh)/t^2 is below 2 for n=2 and at most 3/2 for n>=3. The covariance signs follow from 0<h<=t^2 and 0<t<1/2. These arguments include n=2 and every 0<p<1, and establish positive definiteness and all strict signs. The supplied checker.py was inspected, not executed; VERIFICATION.md records 2250 exact assertions for 2<=n<=6 and p in {1/5,1/2,4/5}, which is corroboration only. The symbolic check does not depend on that run.

## originality

PASS

The weighted edge-cover measure is established, and the occupied-box catalogue result uses related linear-residual terminology. Neither gives the stated closed inverse or the joint covariance/linear-partial-correlation sign law for weighted K_{2,n}. No equivalent coverage was found in the checked evidence; this is not a priority determination.

## value

PASS

K_{2,n} is a natural weighted cover family of growing degree with three distinct pair types, including two inequivalent types of incident edges. The exact inverse provides a nontrivial uniform residual-dependence result: the disjoint-edge sign survives linear adjustment for all other edges, even though the disjoint pair factors after literal conditioning on those edges. The proof separates marginal effects of coverage from effects of inversion and gives exact formulas useful as a benchmark for larger cover models. This is not a mixing, association or nonlinear-dependence theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
