# Independent mathematical audit

## correctness

PASS

In the normalized process the stationary coordinate is the stable harmonic filter of U, and a common first redraw followed by exponential contraction gives uniqueness. The finite polynomial generator is closed. Independent scalar recursion on monomials and their tilted stationary initial moments reproduces the complete rational transform symbolically (python3 /workspace/reproductions/finite_checks.py 3). Writing its numerator as H(s+1)+B gives A=Kf4(H+BR), where f4 is the fourfold exponential convolution and R=f5/f4. For strict simplicity, more than just strict monotonicity of R is needed: log f4 is concave and analytic on positive t, so its derivative is nonincreasing and cannot agree at distinct positive arguments; agreement would force an interval, and by analyticity global constancy, contradicted by f4(t)∼t³/6. Thus differentiating the defining integral for R gives strictly positive integrand for 0<u<t; the endpoint term vanishes since f4(0)=0 and the derivative is integrable there. Hence R'>0. Its initial limit is zero; its tail is 1/(1−alpha) if alpha<1, grows linearly at alpha=1, and diverges for alpha>1 by the slower e^(−t) factor. B is positive in d≤4; for d≥5 and alpha≥1 the strict crossing condition is B<0. For alpha<1 the tail sign is that of 3(d+1)−3(d−2)alpha−(d−1)alpha², decreasing for d≥5 with value 10−d at one. If its limiting sign is zero the finite-time factor stays strictly positive, while a negative limit gives exactly one simple crossing. This handles the equality cases and repeated decay rates without dividing by pole differences. The d=11 threshold is 0.978626204439…, as stated.

## originality

PASS

The all-dimension and all-rate sign classification with its sharp piecewise threshold and simple crossing is distinct on the inspected evidence. Stationary moments, polynomial resolvents and the observable as a general irreversibility witness are not the novelty claim. Two later indexed results directly overlap on genuine slices, and two same-day records have strong partial overlap in either the dimension threshold or the observable, but not both with the same stationary model.

## value

PASS

A single exact statistic detects a qualitative difference invisible in stationary even moments: the sign develops a unique lag reversal only from dimension five onward, with a sharp rate criterion and a change in the formula for that criterion. This is a usable sign and uniqueness theorem, stronger than calculating a correlation at a few lags or announcing a numerical transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
