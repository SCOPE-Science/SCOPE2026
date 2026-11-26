# Independent mathematical audit

## correctness

PASS

Removing the conditioned root gives k ordered nonempty trees on n vertices, preserving exactly the designated unary count. Independently, if H=x(1+wH+H^2/(1-H)) marks vertices by x and unary vertices by w, Lagrange inversion gives [x^n]H^k=(k/n)[z^(n-k)](1+wz+z^2/(1-z))^n. Taking [w^u] and normalizing at w=1 gives the asserted PMF. For e=n-k, only strings with e ones and all other entries zero attain e; e-1 unary vertices cannot use the remaining one edge. Thus the tail at e-1 equals binom(n,e)/binom(2n-k-1,e), and the next-root-degree tail there is binom(n,e-1)/binom(2n-k-2,e-1). Their ratio is (2n-k-1)/(k+1), strictly above one exactly for e>1; at e the inequality reverses. The e=1 and e=0 laws are point masses at 1 and 0, and n=3 is the first nonterminal comparison. An independent bounded enumeration by Dyck words confirmed the ratios and support gaps for n=2 through 8.

## originality

PASS

The underlying forest count and profile extraction are standard. The supported distinct claim is the complete adjacent-degree incomparability, with a universal two-threshold witness and the deterministic exception, not a new method to count degree profiles. No exact or stronger comparison was established in the sources inspected.

## value

PASS

Increasing the root degree removes one available forest edge, so a decreasing unary count is a natural proposed stochastic comparison. The sharp reversal at the penultimate threshold shows that this support argument fails for every nonterminal adjacent pair, unlike the ordered leaf statistic in the same model. The result supplies a complete finite-size obstruction and specifies where a stochastic-dominance argument cannot be used; the standard coefficient extraction alone is not the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
