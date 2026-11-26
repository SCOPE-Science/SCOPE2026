# Independent mathematical audit

## correctness

PASS

For the specified completed two-half-step map the coefficient of (hL)^k is (-1)^k[(k+1)/2^{k-1}-1]. In particular the cubic cancels and the fourth coefficient is -3/8. At distance 1 and 2 the first nonzero coefficients are positive, and diagonals tend to one. For distance-three u,v, factoring L^4 as L^2 L^2 independently recovers the key identity: at a midpoint i in U=N(u), (L^2)_{ui}=-|U|-1-p_i-|N(i)∩W|, while (L^2)_{iv}=p_i. V=N(v) gives the symmetric terms; W contributes x_w y_w, and the endpoints contribute zero. Keeping one cross edge and deleting others increases this expression. Conditioning on whether w meets the two surviving edge endpoints gives exactly max(0,ab-2) as its maximal contribution for |U|=a, |V|=b. Balancing a,b for each sum and evaluating the short bound tables gives -1 and 4. Independent integer matrix-vector Laplacian iteration and breadth-first distances on the two witnesses confirm both equality cases have diameter 3. The fourth-order coefficient of the failing entry is -3/2. The sign rule at distance three requires a nonzero fourth coefficient; the bounds and witness used in the theorem satisfy this, but one cannot apply that rule to a general pair with vanishing coefficient.

## originality

PASS

Known extrapolation and known positivity failures do not establish the minimum order under the frozen graph restriction, nor the two sharp pairwise bounds. No inspected source gives or implies that distinct claim. This is a bounded literature judgment, not proof of priority.

## value

PASS

The cubic cancellation creates a natural boundary where graph distance alone no longer decides the sign. The extremal argument explains which cross edges and common midpoints can make the first surviving coefficient negative in the update; it proves protection of every smaller graph in scope, not just a witness. This is useful for understanding loss of positivity under second-order acceleration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
