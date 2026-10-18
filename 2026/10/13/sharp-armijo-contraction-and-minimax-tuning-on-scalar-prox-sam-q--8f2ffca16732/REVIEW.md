# Independent mathematical audit

## correctness

PASS

On H(x)=lambda(x-x*)^2/2 and R=0 the scalar scaled gradient trial direction is d=-r e; the paper's proximal model decrement is q=-lambda*r*e^2/2. With nonstationary e, the source Armijo inequality (1-tr)^2<=1-eta*tr is equivalent to tr<=2-eta. Geometric backtracking has accepted u=r if r<=2-eta, else beta(2-eta)<u<=2-eta. Thus 0<u<2 and |e_next|/|e|=|1-u|<=max(1-min{r0,beta(2-eta)},1-eta)<1 for all r>=r0. Extremal raw steps r=r0 when available, r=(2-eta)/beta^j, and near-rejected boundaries demonstrate sharpness under only r>=r0; optimizing gives eta*=min(r0,2beta/(1+beta)). Checked eta in (0,1), beta in (0,1), r0>0 and unbounded r allowed. The case e=0 is stationary and excluded from cancellation.

## originality

PASS

Earlier generic Armijo descent analysis contains scalar test ingredients, but the identified source-specific sharp contraction envelope with its lower-raw-curvature information class and exact minimax eta was not located as a theorem in the inspected primary article or targeted literature. The result is conditional and a special application; this is best-of-knowledge originality, not a claim to invent Armijo backtracking.

## value

PASS

Sharp worst-case contraction for the source's *separate* raw learning rate/variable metric and geometric line-search relaxation is a motivated exact scalar algorithm benchmark. The minimax eta exposes the r0-limited vs backtracking-limited transition, not just convergence; it is meaningful for diagnosing stability when raw curvatures are uncontrolled above. It does not claim stochastic, multidimensional or empirical tuning guarantees. Its derivation is elementary, so the value is deliberately narrow but mathematically operational rather than a generic textbook restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
