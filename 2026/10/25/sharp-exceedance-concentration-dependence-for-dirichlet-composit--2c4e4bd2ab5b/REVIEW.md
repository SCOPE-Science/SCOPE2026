# Independent mathematical audit

## correctness

PASS

For X~Dirichlet(alpha_1,...,alpha_m), m>=2 and all alpha_j>0, neutrality gives Y=X_i~Beta(a,b) and g(x)=E(Q_q|Y=x)=x^q+c_i(1-x)^q, q>1. The covariance is the tail integral H(t)=int_t^1(g(x)-mu_q)f_beta(x)dx with H(0)=H(1)=0. Strict convexity, g(1)=1>mu_q and unique minimum below mu_q give exactly one positive H regime when c<=mu, or exactly one H zero with negative-to-positive switch when c>mu. The symmetric gamma-ratio h(z)=(z)_q/z is strictly increasing, so c>mu for all q>1 and symmetric m. For q=2, differentiated expression (1+c)t(1-t)f_{a,b}(t)(t-theta)/(A+1) satisfies H prime and endpoint; theta=(c(a+2b+1)-(a+1))/(A(1+c))<1. Substitution gives symmetric theta=(alpha+1)/(m alpha+2), uniform spacings theta=2/(m+2), scaling s(s-2)e^-s, and heterogeneity boundary a=4u+3. Independently computed 72 exact rational beta-tail integrals, separate from beta-derivative method. No inference about arbitrary asymmetric K_t covariance or q=1.

## originality

PASS

Dirichlet beta neutrality, marginal Greenwood distributions (Royen) and beta Stein integration (Goldstein-Reinert) are prior tools. Huillet-Paroissin quantify sampled-species richness conditional on latent masses, a different random variable from counting Dirichlet mass exceedances. The standalone covariance one-switch/no-switch theorem, symmetric all-real-q assertion and explicit asymmetric boundary were not implied by the inspected primary theorems. Nearby published findings on finite-sample richness/Gini-Simpson covariance and fixed-ball occupancy signs are different experiments. Classical Greenwood/spacing or beta Stein literature might conceal the same joint formula, so originality is best-knowledge and qualified.

## value

PASS

The exceedance count and concentration power sum are standard complementary diagnostics of random partitions/spacings. The theorem supplies the entire threshold sign diagram, all real powers q>1 in the symmetric family, a sharp broken-stick switch at 2/(m+2) and rescaled limit, and a heterogeneous parameter boundary where reversal disappears. This is a natural continuous classification, not a handful of fitted examples or an arbitrary scalar covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
