# Independent mathematical audit

## correctness

PASS

For u=x/b the left fixed-point equation is h_b(u)=1−a, h_b(u)=(1−bu)/cos(πu/2). Its derivative numerator Q_b goes from −b to (π/2)(1−b), and Q'_b=(π²/4)(1−bu)cos(πu/2)>0. Thus h_b drops from 1 to its unique minimum m_b and increases to infinity, giving exactly the advertised intersections for levels in (0,1). Reflection of the interior fixed-point equations gives c=h_(1−b)((1−x)/(1−b)), not a global conjugacy of the discontinuous map. The endpoints and assigned switch value are not fixed. Both interior branches have positive multipliers. Strict convexity/concavity of F−x gives the stated ordering of slopes in the two-root cases, and at tangency F'=1, F''≠0 and the respective a or c derivative is a positive cosine. At the left fold the displacement is positive on either side, so it attracts from the left and repels to the right locally; the signs reverse at the right fold. Evaluating h at the previous minimizer proves strict decrease of m_b in b; h_1(u)=(1−u)/sin((π/2)(1−u))>2/π, and continuity at each fixed u<1 followed by u→1 gives the limiting minimum 2/π. The implicit root near (b,u)=(0,0) is analytic and odd in b because Q_(−b)(−u)=−Q_b(u), so u_b=4b/π²+O(b³) and m_b=1−2b²/π²+O(b⁴); reflection gives the other endpoint law. The exact rational witness follows from 3·297²=264627>250000=500², testing x=1/6 and 5/6 and the branch ends. This proves the closed census on the stated open parameter cube, all-breakpoint coexistence, and local stability, not full basins or higher periods. The deposited verifier was inspected, not executed; its finite grid is supplemental.

## originality

PASS

Lawnik–Moysis–Volos already state the exact map, branch geometry and numerical fixed-point-free regions. An earlier indexed result proves an exact two-fold census with identical local stability ordering for the fractional-power member, but its threshold formulas and breakpoint restrictions do not imply those for cosine. The supported distinct part is the exact cosine-specific partition and endpoint constants, in particular two sinks attainable at every interior breakpoint. The judgment does not grant novelty to generic convex/concave root counting.

## value

PASS

The original cosine family's published numerical equilibrium-free diagrams leave a natural exact classification gap. The sharp thresholds let a researcher choose or exclude fixed points and simultaneous sinks without parameter-grid uncertainty, including near either highly asymmetric breakpoint. Equality cases and the quadratic size of the coexistence windows at the corners add information not recoverable from a representative four-point example or the generic curvature bound. Value is local fixed-point geometry, not a claim about global chaos or security.

The dated certificate retains the supplied scientific assessment, sources and limitations.
