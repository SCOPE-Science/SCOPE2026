# Independent mathematical audit

## correctness

PASS

The source rational stability map has an analytic Jordan Taylor expansion R(hJ_n)=sum_{k=0}^{n-1}(h^k/k!)R^(k)(-h)N_n^k. The shift powers occupy disjoint subdiagonals, making each derivative sign necessary and sufficient. The explicit derivative bracket is 1+sqrt(2)-k+(3+2sqrt(2))h, strictly decreasing in k, so the last k=n-1 gives the iff including n<=3 and h=0 boundary. Independent symbolic coefficient/surd checks confirmed n=4 h=1/20 negative and h4=10-7sqrt(2), not merely a sampled experiment.

## originality

PASS

Original ROS2 source gives scalar R and positive negative-real values; later work identifies the first two positive derivatives and a third derivative obstruction, so these ingredients are prior. Neither known general absolute-monotonicity statement implies the exact Jordan-subdiagonal iff plus re-entrant h>0 recovery; best-of-knowledge searched equivalents absent.

## value

PASS

Motivated sharp positivity frontier for an exact positive serial-decay semigroup and widely used stiff integrator. Shows a genuine state-count threshold and counterintuitive restoration at large steps, not a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
