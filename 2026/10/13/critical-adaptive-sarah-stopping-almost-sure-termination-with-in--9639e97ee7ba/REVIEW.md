# Independent mathematical audit

## correctness

PASS

For exact scalar f1=x²/2,f2=3x²,F=7x²/4,η=1/2,γ=1/4, the recursive gradient v_t=(1−η a_I)v_(t−1) is multiplied independently by 1/2 or −2, so log2|v_t/v0| is a simple symmetric walk; first threshold hit T of −1 has Catalan law C_j/2^(2j+1), a.s. finite and infinite expectation. On the disjoint all-up-then-down strings E_h of probability 2^(−2h−1), the signed iterate sum equals (5/3)(−2)^h+1/3−(−1)^h/2, giving |x_{T+1}|≥2^h|x0|, so E[x²]=∞ and finite-cap E[x_{min(T,N)+1}²]≥x0²/2 floor((N−1)/2). Independent exact rational rare-path checks h=1..12 confirmed signs and amplitude inequality; the infinite conclusion uses symbolic formulas and disjoint events. Inspected Algorithm 2 order: output is w_t after t increment, agreeing with source indexing when uncapped.

## originality

PASS

PASS for coupling a critical, oscillating recursive-gradient first-passage time to unbounded signed returned-iterate risk in an exact SARAH+ inner pass. The original published Algorithm 2 has a mandatory finite cap and so has no infinite expected work; those finite capped loops are explicitly excluded. A published related Resultary SARAH infinite-loop result finds a residual floor under a different stable-magnitude construction; it neither implies this Catalan stopping tail nor the infinite second moment.

## value

PASS

Provides a precise and motivated failure mode for a natural uncapped adaptive stopping heuristic and quantifies linear growth of second-moment risk under increasing finite caps despite full-gradient descent stability. This is a mathematical boundary result, not a claim against the finite published algorithm or its safe η convergence guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
