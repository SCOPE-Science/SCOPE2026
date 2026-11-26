# Independent mathematical audit

## correctness

PASS

For each ordered dimension profile the stabilizer is the product of the block general linear groups (including the trivial size-zero factors). Multiplying the orbit size by the number of blockwise nilpotents cancels all q-powers on division by the total nilpotent count, giving (1). The latter count can also be derived directly: partition all endomorphisms by the canonical nilpotent/invertible Fitting splitting and divide by |GL_n| to get 1/Q_n = sum_{d=0}^n (#nilpotents in dimension d)/|GL_d|; first differences give the required q^(n²−n). The error per profile in replacing the ratio by Q_infty^(1−k) is O(q^(−n)+sum_i q^(−r_i)), summing to O(n^(k−2)) at fixed q,k. This proves the mean and gives O(1/n) total variation on the discrete profile space after normalizing pair weights; the uniform lattice simplex converges weakly to Dirichlet(1,…,1). This is not a conditional-uniform splitting law under a uniform matrix. Indecomposability is exactly one Jordan block, so exactly those matrices attain the minimum k. Their orbit gives (3); strict majority follows for q≥2 and n≥3 by bounding the product below by (3/4)(7/8)(1−sum_{i≥4}2^(−i))=147/256; n=1,2 are immediate. In k=2 the invariant complementary spaces and commuting projections are bijective. Independent finite reproduction: python3 /workspace/branches/125cefa1-8276-4ce4-8c93-941c6f042ab1/independent_counts.py (output independent_counts.out in the same directory). Direct matrix/idempotent enumeration matched all k=2 ranks and k=3 profiles at (n,q)=(2,2),(3,2),(2,3), including 64 nilpotents, rank totals 64,112,112,64 and 42 regular nilpotents at (3,2). Those checks do not certify the limits or constitute formal verification.

## originality

PASS

Pass for the actual synthesis: the dimension-profile mean, quantitative approach to the uniform composition law under pair sampling, and the contrast between polynomial annealed mean and one-block rigidity under uniform matrix sampling. The product probability in (3) is exactly covered already and gets no originality credit, nor do the Gaussian multinomial, classical nilpotent count or one-block centralizer calculation in isolation. No inspected source states or supplies a dominating result for the combined splitting laws under the two stated measures.

## value

PASS

A natural statistic of nilpotent centralizers (idempotent ranks or several invariant direct summands) has sharply different behavior under two canonical measures. The exact jointly indexed mean explains the difference and supplies the lattice rate and the continuum profile law even when a strict majority of uniform matrices has no nontrivial split. The increment is this quantitative comparison, not the known regular probability or a renamed Gaussian coefficient alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
