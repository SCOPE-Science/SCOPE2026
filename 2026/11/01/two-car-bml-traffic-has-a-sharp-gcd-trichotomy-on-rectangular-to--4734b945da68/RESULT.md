# Two-car BML traffic has a sharp gcd trichotomy on rectangular tori

## Finding

Consider the east-then-north Biham–Middleton–Levine (BML) traffic automaton on a rectangular periodic grid with \(m\ge 2\) columns and \(n\ge 2\) rows, containing exactly one eastbound car \(H\) and one northbound car \(V\), initially at different sites. Set \(g=\gcd(m,n)\) and \(L=\operatorname{lcm}(m,n)\). The following classification holds for **every** initial placement.

1. If \(g\ge3\), there is at most one blocked half-step in the entire future, after which both cars move on every update. The eventual primitive period is \(L\), with speeds \((v_H,v_V)=(1,1)\). Among the \(mn-1\) different valid relative placements, exactly \(2L-1\) experience one block, and the other \((g-2)L\) never experience one.
2. If \(g=2\), every trajectory eventually reaches a periodic sequence of exactly one blocked eastbound move and one blocked northbound move per period. The primitive full-configuration period is \(L+1\); both speeds are \(L/(L+1)\).
3. If \(g=1\), define the unique integer \(r\in\{1,\ldots,n-1\}\) satisfying \(mr\equiv1\pmod n\). Every trajectory eventually reaches a periodic orbit with blocks of just **one** species. If \(2r>n\), only \(H\) is blocked, once every \(P=m(n-r)+1\) updates, and \((v_H,v_V)=(1-1/P,1)\). If \(2r\le n\), only \(V\) is blocked, once every \(P=mr\) updates, and \((v_H,v_V)=(1,1-1/P)\). The given \(P\) is the primitive period of the full configuration.

Here an update means a complete eastbound half-step followed by a northbound half-step, and a speed is the asymptotic fraction of the corresponding car's attempted moves that succeed. In particular, coprime rectangles have infinitely many blocks despite having just two cars, even as their density \(2/(mn)\) tends to zero. In contrast, square tori of side at least three become fully flowing with at most one block.

## Assumptions and scope

Coordinates are \((x,y)\in\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\). Every complete update first lets \(H\) attempt to move from \((x_H,y_H)\) to \((x_H+1,y_H)\), remaining stationary if that site contains \(V\). Afterwards \(V\) attempts to move from \((x_V,y_V)\) to \((x_V,y_V+1)\), remaining stationary if the destination then contains \(H\). The cars cannot share a site. The order of the two substeps is part of the definition. There are no other cars, boundary injections, randomized updates, or simultaneous conflict-resolution rules. Speeds are measured in moves per complete update, not per half-step.

A *blocked* move is one attempted move prevented by occupancy. A *primitive full-configuration period* is the least positive number of complete updates that returns both labeled cars to their original respective positions on their eventual periodic orbit. All claims concern finite integer \(m,n\ge 2\), without any asymptotic restrictions.

## Proof

**1. Exact relative-state reduction.** Define \(a=x_V-x_H\pmod m\) and \(b=y_H-y_V\pmod n\). The admissible relative states are the \(mn-1\) elements of \((\mathbb Z/m\mathbb Z)\times(\mathbb Z/n\mathbb Z)\) other than \((0,0)\). Direct inspection of the two ordered substeps gives

\[
 R(a,b)=\begin{cases}
 (1,-1),&(a,b)=(1,0)=:A,\\
 (0,1),&(a,b)=(1,1)=:B,\\
 (a-1,b-1),&\text{otherwise}.
 \end{cases}
\]

At \(A\) the eastbound car alone is blocked; at \(B\) it moves but the northbound car is blocked. These two exceptional cases are disjoint because \(n\ge2\). The zero relative state is never reached from a valid state: the only would-be free predecessor of \((0,0)\) is \(B\), and its actual image is \((0,1)\). Thus \(R\) exactly models the physically permitted dynamics for all time.

Let \(U(a,b)=(a-1,b-1)\). Every \(U\)-orbit has exactly \(L\) states. Two relative states lie on the same free orbit precisely when \(a-b\) agrees modulo \(g\), where subtraction of residues is well-defined modulo their common divisor. Write this invariant as \(d\in\mathbb Z/g\mathbb Z\). The exceptional points have \(d(A)=1\) and \(d(B)=0\), whereas their images have \(d(R(A))=2\) and \(d(R(B))=-1\).

**2. The case \(g\ge3\).** Both images of exceptional points have classes outside \(\{0,1\}\). In all other classes the evolution is forever \(U\), so an orbit has at most one block. Every valid state in class \(1\) traverses \(A\) within a free revolution, and every valid state in class \(0\) traverses \(B\) within a free revolution. The only excluded point in class \(0\) is \((0,0)\); no valid initial state reaches it before its exceptional point. Because each class has \(L\) states, the count of relative placements that ever block is exactly \(L+(L-1)=2L-1\), and the nonblocking count is \((g-2)L\). After its possible block every orbit advances both cars one site per complete update. Its relative and full-configuration primitive period is then \(L\), since the simultaneous shift has order \(L\) on the \(m\)- and \(n\)-cycles.

**3. The case \(g=2\).** The two exceptional jumps exchange the two free classes: \(A\) moves from class \(1\) to class \(0\), and \(B\) moves from class \(0\) to class \(1\). Each class consists of one length-\(L\) free cycle and contains its respective exceptional point, so every valid orbit eventually alternates the two types of block. To determine the exact length, write \(m=2u\), \(n=2v\) with \(\gcd(u,v)=1\). Immediately after an \(A\)-block the relative state is \((1,-1)\). Before the next \(B\)-block it makes \(mk\) ordinary free steps, where \(k\in\{0,\ldots,v-1\}\) is determined by \(uk\equiv-1\pmod v\). Immediately after a \(B\)-block the state is \((0,1)\). Before the next \(A\)-block it makes \(mj-1\) ordinary free steps, where \(j\in\{1,\ldots,v\}\) satisfies \(uj\equiv1\pmod v\). This includes \(v=1\), with \(k=0\), \(j=1\). In all cases \(k+j=v\). Counting the blocking updates, the recurrence time is

\[
 (mk+1)+(mj)=mv+1=L+1.
\]

Within this interval each car misses exactly one move. It therefore advances \(L\) sites, a multiple of its own circumference. Hence the complete configuration closes after \(L+1\) updates. The relative orbit sees each exceptional state exactly once, proving that no shorter return is possible. Both average speeds are \(L/(L+1)\).

**4. The case \(g=1\).** There is only one free class; every valid initial state must encounter \(A\) or \(B\) after finitely many free steps. Let \(r\in\{1,\ldots,n-1\}\) satisfy \(mr\equiv1\pmod n\).

After an \(A\)-block, the relative state is \((1,-1)\). The number of subsequent free steps needed to reach \(A\), respectively \(B\), is

\[
 t_{A\to A}=m(n-r),\qquad
 t_{A\to B}=m\bigl((-2r)\bmod n\bigr),
\]

where the second residue is chosen in \(\{0,\ldots,n-1\}\). Thus \(B\) comes first when \(2r\le n\), and \(A\) comes first when \(2r>n\). After a \(B\)-block, the state is \((0,1)\). The corresponding free-step counts before reaching \(A\), respectively \(B\), are

\[
 t_{B\to A}=mj-1,\qquad t_{B\to B}=mr-1,
\]

where \(j\in\{1,\ldots,n\}\) is the positive representative of \(2r\pmod n\). When \(2r\le n\), one has \(j>r\), including the boundary \(2r=n\) at which \(j=n\), so \(B\) comes first. When \(2r>n\), one has \(j=2r-n<r\), so \(A\) comes first. These comparisons prove that both possible first block types enter the same eventual single-species blocking cycle.

If \(2r>n\), the time between \(A\)-blocks is \(P=m(n-r)+1\). The eastbound car moves \(P-1=m(n-r)\) times, divisible by \(m\), and the northbound car moves \(P\) times, divisible by \(n\) since \(mr\equiv1\pmod n\). If \(2r\le n\), the time between \(B\)-blocks is \(P=mr\); the eastbound car moves \(P\) times, divisible by \(m\), and the northbound car moves \(P-1\) times, divisible by \(n\). Hence these are full-configuration periods. In either case no earlier relative-state return is possible along the intervening ordinary free segment, and there is exactly one exceptional point per period; the periods are primitive. The stated speeds follow from the one missed move per period. This completes the trichotomy.

## Verification

The standalone file `verify_two_car.py` performs independent, exact-integer checks using the **physical positions** of both cars and the ordered occupancy rules, not the derived relative-state map. It enumerates all \(18{,}000\) valid translation classes across all \(225\) pairs \(2\le m,n\le16\), computes the eventual primitive full-state period by detecting repeats, verifies the number and types of blocked steps per period, and checks the \(2L-1\) initial-placement count whenever \(g\ge3\). All checks pass. This finite computation is a diagnostic; the four proof steps above establish the theorem for arbitrary grid dimensions. Run it using `python3 verify_two_car.py` with Python 3.8 or later; only the standard library is needed.

## Relationship to prior work

Hertzberg Rabinovich, Biham and Katzav study the low-density square-grid BML model, particularly its convergence to free-flowing states and the relevance of interactions between opposite-direction car pairs [1]. Their analyzed parameter space is a square grid with many cars; the complete two-car **rectangular** gcd-dependent orbit and speed theorem above is not a consequence of their stated results or appendices.

D'Souza demonstrates aspect-ratio-dependent periodic, partially jammed bands on rectangular tori, notably for coprime dimensions, and develops geometric speed estimates at intermediate densities [2]. These results do not count the complete two-car trajectories or predict the exact gcd trichotomy. Austin and Benjamini prove that fewer than half the side length of cars on a **square** torus always eventually move freely [3]. The square case of the present result is compatible with that theorem; its coprime-rectangle persistent blocks show why the square restriction matters. General periodicity and model rules are classical and are not claimed as new. The novelty asserted is the *combined exact two-car theorem* stated above, subject to the priority limitation below.

## Limitations

This result concerns exactly two cars of opposite orientations, with ordered east-then-north updates and periodic rectangular boundaries. It does not determine the positive-density phase diagram, the dynamics with multiple cars of either species, or different update conventions. It establishes no independent mathematical audit or exhaustive guarantee against unindexed literature on dilute traffic automata. The physical-state program tests finitely many dimensions; the all-dimensional claim is supported by the analytical argument.

## References

1. G. Hertzberg Rabinovich, O. Biham, and E. Katzav, *Structure and dynamics in the low-density phase of a two-dimensional cellular automaton model of traffic flow*, arXiv:2601.01180 (first posted January 3, 2026), https://arxiv.org/abs/2601.01180 .
2. R. M. D'Souza, *Coexisting phases and lattice dependence of a cellular automaton model for traffic flow*, Physical Review E **71** (2005), 066112, https://doi.org/10.1103/PhysRevE.71.066112 . Lawful open-access author copy: https://web.cs.ucdavis.edu/~raissa/Pubs/bml-pre.pdf .
3. T. D. Austin and I. Benjamini, *For what number of cars must self organization occur in the Biham-Middleton-Levine traffic model from any possible starting configuration?*, arXiv:math/0607759 (first posted July 31, 2006), https://arxiv.org/abs/math/0607759 .
