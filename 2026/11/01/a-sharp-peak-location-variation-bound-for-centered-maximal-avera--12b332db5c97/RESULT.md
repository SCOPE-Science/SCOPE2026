# A sharp peak-location variation bound for centered maximal averages on finite paths

## Finding
Let \(n\ge3\), and let \(f:\{1,\ldots,n\}\to[0,\infty)\) be unimodal: for some \(k\in\{1,\ldots,n\}\),
\[
f(1)\le\cdots\le f(k)\ge\cdots\ge f(n).
\]
For the counting-measure centered Hardy--Littlewood maximal operator on the path \(P_n\), write
\[
(Mf)(i)=\max_{r\in\mathbb Z_{\ge0}}\frac{1}{|B(i,r)|}\sum_{j\in B(i,r)}f(j),\qquad
B(i,r)=\{j:1\le j\le n,\ |j-i|\le r\}.
\]
Define \(\operatorname{Var}(g)=\sum_{i=1}^{n-1}|g(i+1)-g(i)|\). Put \(H=f(k)\), \(a=f(1)\), and \(b=f(n)\). Then \(Mf\) is nondecreasing through \(k\), nonincreasing thereafter, and \((Mf)(k)=H\). In particular,
\[
\boxed{\operatorname{Var}(Mf)=2H-(Mf)(1)-(Mf)(n)}.
\]
The following **peak-location inequality** holds:
\[
\boxed{\operatorname{Var}(Mf)\le
\operatorname{Var}(f)-\frac{H-a}{k}-\frac{H-b}{n-k+1}.}\tag{1}
\]
For every \(n\ge3\) and every peak location \(k\), equality in (1) occurs for the single-spike input \(f=\mathbf1_{\{k\}}\). Thus the two endpoint-loss coefficients in (1) have simultaneous sharpness witnesses. Consequently,
\[
\boxed{\operatorname{Var}(Mf)\le\left(1-\frac1n\right)\operatorname{Var}(f)}\tag{2}
\]
for every nonnegative unimodal input, and the unrestricted constant within this class is exactly \(1-1/n\), attained by \(f=\mathbf1_{\{n\}}\) or its reflection. In the genuinely one-peaked case \(1<k<n\) and \(H>a,b\), inequality (2) is strict and has the explicit quantitative deficit
\[
\left(1-\frac1n\right)\operatorname{Var}(f)-\operatorname{Var}(Mf)
\ge(H-a)\left(\frac1k-\frac1n\right)
+(H-b)\left(\frac1{n-k+1}-\frac1n\right)>0.\tag{3}
\]

## Assumptions and scope
The graph is the finite, simple, unweighted path with vertices \(1,\ldots,n\), graph distance \(|i-j|\), counting vertex measure, and unweighted edge variation. The maximal operator averages **nonnegative** data over all integer-radius centered balls, including truncated balls at endpoints. The input is weakly unimodal with a specified (not necessarily unique) peak index \(k\). No corresponding assertion is made here for arbitrary oscillatory inputs, arbitrary signed inputs without taking absolute values, weighted vertex measures, or other graphs. For signed inputs whose absolute values are unimodal, the bound (2) also follows since \(M f=M|f|\) and \(\operatorname{Var}(|f|)\le\operatorname{Var}(f)\); inequality (1) is stated for nonnegative data.

## Proof
**Peak preservation.** Fix \(i<k\). Choose any radius \(r\ge0\) realizing \((Mf)(i)\). If \(r=0\), then \((Mf)(i)=f(i)\le f(i+1)\le(Mf)(i+1)\). If \(r\ge1\), compare the ball \(B(i,r)\) with \(B(i+1,r-1)\). Their right endpoints are identical, and the latter is obtained from the former by deleting zero, one, or two of the leftmost vertices (this remains true when a ball is truncated at an endpoint). Every deleted vertex \(j\) satisfies \(j\le i\), hence \(f(j)\le f(i)\le(Mf)(i)\). Deleting values no larger than their average cannot decrease that average. Consequently \((Mf)(i+1)\ge(Mf)(i)\).

Dually, for \(i\ge k\), choose a maximizing radius for \((Mf)(i+1)\). With radius decreased by one and center moved to \(i\), the left endpoint stays fixed while zero, one, or two rightmost values, each at most \(f(i+1)\le(Mf)(i+1)\), are deleted. Hence \((Mf)(i)\ge(Mf)(i+1)\). The radius-zero case uses \(f(i)\ge f(i+1)\). As all ball averages are at most \(H\) and the singleton at \(k\) has average \(H\), we get \((Mf)(k)=H\). Therefore the variation of \(Mf\) telescopes from the two endpoints to its peak, giving the first boxed identity. The input itself has \(\operatorname{Var}(f)=2H-a-b\).

**Endpoint gains.** The ball centered at vertex \(1\) with radius \(k-1\) is the prefix \(\{1,\ldots,k\}\). Its average is at least \(a+(H-a)/k\) because all prefix entries are at least \(a\) and the \(k\)-th entry is \(H\). Likewise, the ball centered at \(n\) with radius \(n-k\) is the suffix \(\{k,\ldots,n\}\), and its average is at least \(b+(H-b)/(n-k+1)\). Thus
\[
(Mf)(1)-a\ge\frac{H-a}{k},\qquad
(Mf)(n)-b\ge\frac{H-b}{n-k+1}.
\]
Subtracting these inequalities from \(2H-a-b\) proves (1). Since \(k\le n\) and \(n-k+1\le n\), the sum of endpoint gains is at least \((2H-a-b)/n\), yielding (2). Subtracting the latter weaker gains from the stronger two endpoint gains gives (3), whose right-hand side is positive for an interior strict peak.

**Sharpness.** For \(f=\mathbf1_{\{k\}}\), the largest ball average at vertex \(1\) is exactly \(1/k\) (the shortest prefix containing the spike), and at vertex \(n\) it is exactly \(1/(n-k+1)\). Thus (1) is an equality for every peak location. For \(k=n\), the input variation is \(1\), and the output varies monotonically from \(1/n\) to \(1\), with variation \(1-1/n\). Reflection gives the other extremizer. This proves sharpness of (2) within the claimed class.

## Verification
The accompanying `unimodal_verify.py` uses exact rational arithmetic. It exhaustively tests 4,332 unimodal integer sequences of lengths \(3\) through \(8\) with entries in \(\{0,1,2,3\}\), then tests 4,800 deterministic longer integer sequences and 5,047 exact single-spike examples with orders through \(100\). It checks output unimodality, the telescoping variation identity, the peak-location bound, the strict interior-peak deficit, and the global constant. Every check passed. Finite tests are consistency checks only: the preceding argument proves the statements for every allowed real input and every integer \(n\ge3\).

## Relationship to prior work
The discrete centered maximal variation problem originates at least in Bober--Carneiro--Hughes--Pierce (first public version 17 May 2010), which established an \(\ell^1\)-to-variation estimate and discussed the stronger variation conjecture on \(\mathbb Z\), not the finite-path peak-location formula. González-Riquelme--Kovač--Madrid (arXiv:2603.12462, first posted 12 March 2026), Conjecture 5, propose the sharp factor \(1-1/n\) for **all** data on finite paths; they provide numerical evidence through order ten but do not prove the general assertion. A published monotone-data result, *Monotone data attain the conjectured path-graph variational constant* (record identifier `2ae83e2401fb`), proves the constant on monotone inputs but explicitly does not control functions with a change of monotonic direction. The present theorem covers all nonnegative unimodal data, including strict interior peaks, and provides an attained peak-dependent quantitative deficit. Bilz--Weigt (arXiv:2107.12404) prove centered maximal-function variation contraction for indicator functions and for certain positive-pointwise-maximal data on \(\mathbb Z\); those hypotheses and the infinite-line operator are distinct from the present arbitrary-height unimodal finite-path theorem. This comparison is not a claim to have settled the full finite-path conjecture.

## Limitations
The full path conjecture for arbitrary nonnegative sequences remains open. The main inequality is a one-input \(1\)-variation inequality, not a two-input Lipschitz bound, and no weighted, cyclic, or higher-dimensional analogue is established. Searches and the material inspected cannot exclude an earlier equivalent elementary argument under different terminology. The mathematical novelty conclusion is provisional pending independent literature assessment.

## References
1. J. Bober, E. Carneiro, K. Hughes, L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030 (first public 17 May 2010), especially Theorems 1--2 and Question B.
2. C. González-Riquelme, V. Kovač, J. Madrid, *Sharp variational inequalities for the Hardy--Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462 (first public 12 March 2026), especially Conjecture 5.
3. C. Bilz, J. Weigt, *The one-dimensional centred maximal function diminishes the variation of indicator functions*, arXiv:2107.12404 (first public 26 July 2021), especially Theorems 1.3 and 1.5.
4. *Monotone data attain the conjectured path-graph variational constant*, published mathematical finding `2ae83e2401fb` (accessed through its public complete statement).
