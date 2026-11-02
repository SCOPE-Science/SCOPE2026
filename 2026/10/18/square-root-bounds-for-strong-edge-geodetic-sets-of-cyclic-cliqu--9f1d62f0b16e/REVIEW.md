# Independent mathematical audit

## correctness

PASS

For G=C_n square K_m, Cartesian shortest-path distance is d_C(x,y)+1_{p != q}, hence every p-to-q geodesic contains exactly one p-to-q clique/rung edge; n such edges need a_p*a_q>=n distinct selected endpoint pairs for each p<q. The product over all layer pairs plus AM--GM gives |S|>=m sqrt(n). For the upper bound k=ceil sqrt(n), s=min(n,2k+6), the full-vertex case s=n is immediate. For s<n take s distinct anchors T={floor(i*n/s)}, 0<=i<s, in every layer. An L-consecutive-residue interval has at least floor(sL/n) anchors, so the i-th predecessor and j-th successor of each target r lie within ceil(i*n/s) and ceil(j*n/s). Setting h=s/2-2=k+1 gives d_left+d_right <= h*n/s+2 <= n/2 for positive i+j<=h; oriented anchor choices yield h(h-1)=k(k+1)>=n *distinct ordered coordinate pairs* whose shortest cycle arc passes through each target rung. Greedy injection handles all n target rungs per fixed unordered layer pair; pair sets across layer pairs are disjoint. Consecutive anchors have gaps <=ceil(n/s)<=n/2 and cover all rim edges with unused, unique same-layer endpoint pairs. For n=k^2,k>=3, equally spaced k anchors in every layer suffice: the ordered anchor pair (i,d), 0<=i,d<k, is assigned the rung ik for d=0; ik+d for 1<=d<=floor(k/2); and ((i-1) mod k)*k+d for larger d. Each rung in each gap has unique offset, yielding bijection onto k^2 rungs; chosen directed arcs are shortest and same-layer consecutive-anchor paths cover all cycle edges without duplicate unordered endpoints for k>=3. Thus |S|=mk, matching lower bound for all m>=2. Independent implementation tested 268 general parameter pairs (n up to 300), 39 square cases (k up to 15), and 338345 cyclic interval instances, checking all vertex endpoints, exact graph distance, no duplicate unordered endpoint pairs, and edge coverage. The infinite theorem rests on the symbolic argument, not these finite tests.

## originality

PASS

Best-of-knowledge originality survives direct statement-level comparison with the exact path--clique result (Klavzar--Zmazek 2024, Thm 3.5), path-grid work, earlier product results, and targeted published-record semantic searches. Matching square-order values do not make the cyclic result a corollary: closing the path introduces shorter reverse arcs and invalidates path routes, and the cyclic rung bijection is independent. No inspected stronger theorem or exact cycle-clique table implies the all-parameter O(m sqrt(n)) bound or square-cycle attainability. Search misses are not proof of historical uniqueness.

## value

PASS

The parameterized strong edge-geodetic set of cyclic clique cylinders is a naturally motivated edge-covering graph invariant; the cycle closure removes the linear shortest-path structure used in the known exact P_n square K_m theorem. Uniform two-parameter upper and lower bounds matching in order Theta(m sqrt n), a constructive approximation factor approaching two independent of clique size, and an exact infinite square-cycle subfamily with an explicit geodesic rung bijection are substantial and independently useful. The construction is not a routine substitution or isolated finite table; it handles every m>=2 and all n>=3, although it leaves nonsquare exact values and optimal leading constant open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
