# Independent mathematical audit

## correctness

PASS

Summing F(q)=sum q^j/(j(j+1)) gives 1+(1-q)log(1-q)/q, so V=F(q)-F(q^2). The derivative is H(q)/q^3 and H=q R(q)/(1-q^2)^2 for R(q)=2q^3-q^2-8q+3 with R'(q)=2(q+1)(3q-4)<0. H initially rises, has one local maximum, decreases to -infinity near q=1, hence exactly one positive zero q* at which V is maximized. Since H'(q*)<0, Taylor gives curvature -H'(q*)/(2q*^3)>0. Boundaries q=0 and 1 have V=0; theta fixed in asymptotic limit. Independent check: Independent symbolic differentiation verified identities V'=H/q^3 and H''=qR/(1-q^2)^2, plus high-precision unique-root location, coefficient maximum, fair coin benchmark and quadratic curvature. The bundled source rational-series root bounds were inspected and are finite rational certificates; uniqueness relies on the cubic-monotonicity proof.

## originality

PASS

Best-of-knowledge priority qualified by primary-source comparisons and explicit antecedent/corollary limits; For the previously established limiting variance V(theta)=sum_{j>=1}q^j(1-q^j)/[j(j+1)] with q=1-theta, there is a unique maximizer theta*=0.32993242521751849..., characterized by H(q*)=0 where H(q)=(2-q)log(1-q)+2log(1+q)+q^2, with Vmax=0.1854345441670716... and sharp quadratic stability curvature 0.6387895185247574...; the original fixed-theta CLT/MDP/LIL are prior work. is not supplied in the compared prior statements.

## value

PASS

Selecting the sampling rate to maximize random-LCM endpoint fluctuations or minimize the fixed-parameter quadratic MDP coefficient is a natural optimization; the nondegenerate unique maximizer, quantitative gain over fair-coin sampling and curvature supply a usable precise design parameter, albeit a modest analytic refinement of a known profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
