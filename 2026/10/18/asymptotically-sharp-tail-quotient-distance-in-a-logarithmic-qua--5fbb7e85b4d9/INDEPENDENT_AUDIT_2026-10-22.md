# Independent mathematical audit

## correctness

PASS

For each finite positive m-coordinate block u and each late-tail v, disjoint supports make ||u-v||_1=m+b where b=||v||_1. A disjoint negative unit block of cardinality m yields F_t≡0 and distance 2m, so q_theta<=2m. If b>=(1-delta)m the l1 term gives >=(2-delta)m. Otherwise S=m+sum w_j satisfies delta*m<|S|<2m for w=-v, and at t=1 the exact identity F_1=-m log m-D-S log(|S|/m), D=sum w_j log(m/max(|w_j|,1)), has |D|<=b log m, |S log(|S|/m)|<=2m log(2/delta). Thus H>=m[delta log m-2log(2/delta)]; for theta times the bracket >=1 the defect contributes at least m and enforces norm >=2m. The explicit delta_m=(3 log log m+10+2/theta)/log m for sufficiently large m has delta_m->0, delta_m<=1/2 and theta[delta_m log m-2log(2/delta_m)]>=1. The proof works for arbitrary absolutely summable complex tails, not just finite or constant-coefficient ones. Berná exact norm m(1+theta log m) and bidual block norm m yield stated ratios. Source finite checker was read but not executed; analytical scale-one argument covers the infinite-dimensional tail infimum.

## originality

PASS

Berná original paper Remark 6.1 proves only m<=q_theta(1_A)<=2m; the missing limiting endpoint is not implied by those inequalities. The published result on exactly the same logarithmic space establishes the different projection/suppression constant k_m(theta)∼log m but neither computes infimum distances to all tails nor supplies a sharp q_theta/m limit. The submitted scale-one entropy obstruction supplies the asymptotic lower endpoint 2. Both complete primary original work and the related public same-space result were inspected.

## value

PASS

Berná specifically introduced the natural tail quotient gauge to reveal a basis obstruction, yet its asymptotic value for every m-coordinate block was left in a nontrivial factor-two interval. Identifying the sharp endpoint and effective logarithmic convergence gives a concrete, independently usable invariant of the natural whole block family and exact coefficient theta/2 for norm-to-gauge distortion. It is not a textbook renaming or an arbitrary slice; resolving a stated sharp gap in a motivated construction suffices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
