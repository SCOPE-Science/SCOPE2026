# Independent mathematical audit

## correctness

PASS

The regionally pooled annual multiplier is s(1-g)+(Bg/k)K with K binomial(k,p), and iid years justify L=E log R as the almost-sure growth exponent for g<1. The all-failure atom of probability (1-p)^k makes L strictly concave and sends L(g) to -∞ at g=1. Its derivative at zero equals (Bp-s)/s, proving boundary/interior uniqueness. For fixed interior g, φ_g(x)=(Bx-s)/(s(1-g)+Bg x) has strictly negative second derivative: deleting one of k+1 Bernoulli observations and Jensen shows L′_{k+1}(g)>L′_k(g), hence g_{k+1}>g_k. A law-of-large-numbers argument at every fixed g<1 gives g_k→1, and an admissible near-one trial plus binomial concentration gives optimal growth→log(Bp). At optimum sE[1/R]=1, separating K=0 from K≥1 and applying exponential small-tail estimates yields (1-p)^k/(1-g_k)→(Bp-s)/(Bp). The explicit k=1 and k=2 optimum algebra is correct. Slow convergence at k=40 is consistent with asymptotics, not a counterexample.

## originality

PASS

Cohen 1966 one-environment delayed-germination optimization, Venable–Brown 1988 joint dormancy/dispersal risk substitution, and Bascompte–Possingham–Roughgarden 2002 geometric-mean benefit from independent patches are genuine background. The exact finite-k interior optimizer, strict ordering for every integer k and sharp reserve asymptotic (Bp/(Bp-s))(1-p)^k are the final claim. Accessible primary materials discuss patch-number persistence, tradeoffs and risk spreading but do not establish this all-integer optimization law with prefactor. The closely relevant full Bascompte article, as well as Venable–Brown 1988, is not fully accessible; compare their actual abstracts and state the remaining overlap risk rather than claiming absence. No strong covered theorem has been found, so best-of-knowledge PASS rather than automatic fail for access.

## value

PASS

The classical dispersal-versus-dormancy intuition asks whether spatial risk spreading can eliminate temporal reserve. This analysis isolates a natural fully mixed Bernoulli patch model and proves an exact answer across every patch count: reserve is always positive yet exponentially small, with a physically interpretable prefactor governed by safe and risky returns. The sharp all-failure boundary matters because an approximate mean-field replacement would predict complete germination. The theorem also quantifies a strict all-k monotone optimal response; these are mathematically meaningful natural invariants, without any claim of empirical field validation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
