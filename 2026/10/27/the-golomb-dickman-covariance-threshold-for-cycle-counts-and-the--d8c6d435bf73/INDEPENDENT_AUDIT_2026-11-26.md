# Independent mathematical audit

## correctness

PASS

For a specified marked j-cycle its occurrence leaves an exactly uniform complementary permutation, and summing its occurrence probability over the candidate cycles gives 1/j. This proves the exact covariance identity, including j=n with the empty complement. Uniform insertion of label r+1 is a bijective sampling rule and grows a chosen longest cycle with conditional probability M_r/(r+1). The uniform length of a tagged cycle gives E M_r >= (r+1)/2, hence each increment of the mean is at least 1/2. For m=n-j >= j, bounding the shortfall below j by that of a uniform tagged cycle gives E[(j-M_m)_+] <= j(j-1)/(2m). Subtract the gain of at least j/2 in E M_n and divide by j to obtain the stated strict negative bound, including the midpoint. For j>n/2 the maximum in the marked identity is j identically. The mean is strictly above n/2 and below n for n>=2, proving the sign, conditional zero criterion, and existence and location of the first positive length. Shepp–Lloyd's mean limit then gives both asymptotic claims.

## originality

PASS

The distinct supported claim is the finite sign boundary for the covariance between the maximum and each exact cycle-length count, together with a uniform short-length bound. The marked moment machinery and longest-cycle limit are classical. None of the checked matches supplies or immediately implies the all-length sign assertion without the shortfall-versus-growth estimate.

## value

PASS

This is a natural joint dependence question for the uniform permutation, not a new evaluation of a classical constant. The theorem resolves every exact length and finite size with one interpretable boundary, identifies the boundary with a known marginal statistic, and gives quantitative control of the entire short-cycle regime. This supplies information neither of the individual marginal distributions conveys by itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
