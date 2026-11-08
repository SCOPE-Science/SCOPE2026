# Independent mathematical audit

## correctness

PASS

For each integer k>=3, binary iid hole selection yields exact finite word weight per all-zero/all-one k-block and a unique decomposition into alternating monochromatic runs. The generating function (1+R_p)(1+R_(1-p))/(1-R_p R_(1-p)) gives the Perron equation A_(k,p)(lambda)A_(k,1-p)(lambda)=1 and gamma=log(2/lambda). Each factor decreases with lambda. At fixed lambda>1 the product derivative with x=p(1-p) is c[(c-2S)(lambda^2-lambda)-S lambda]/(lambda^2-lambda+x)^2<0 because 0<c<=S; the root strictly decreases as x increases, so fair iid switching uniquely maximizes annealed escape. Uniform expansion near lambda=2 proves gamma=2^-k[p/(1+p)+(1-p)/(2-p)]+O(k4^-k), ratio 4/3. At p=0,1 one saturated self-loop remains positive: PF primitivity persists. Quenched rates are not claimed.

## originality

PASS

The general principle of annealed escape as spectral radius of an averaged transfer matrix is prior art (Georgiou–Dettmann–Altmann 2012), and general random-hole quenched pressure is prior art (Atnip et al 2021). The best-of-knowledge new part is an all-depth comparison of iid bias p for complementary run holes, including uniqueness of fair choice and limiting strict 4/3 advantage. Existing fixed-hole / randomized-position formulas do not directly imply the bias derivative or sharp limit, though a weighted renewal analysis could contain it.

## value

PASS

Optimization of escape-rate by controllable iid switching probability between two equally sized holes is a natural open-system design problem. A strict all-depth optimizer and nontrivial exact rare-hole advantage 4/3 quantify value of random switching; neither generic transfer computability nor selected numerics gives this statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
