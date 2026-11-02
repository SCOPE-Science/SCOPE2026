# Independent mathematical audit

## correctness

PASS

Reconstructed the full all-pair minimax. In any normed plane, the two absolute evaluations reduce by signed separation and convex duality to the maximum of distances from 0 to [x,y] and [x,-y]. A symmetric-plane unit isosceles companion is a quarter turn of x; signed permutation symmetry reduces it to x=(u,ru), y=(-ru,u), 0<=r<=1, u=1/(1+ar), a=sqrt(2)-1. The exact piecewise-linear octagon segment optimization and matching dual norm-one functionals yield h(r)=(1+r^2)/(sqrt(2)(1+ar)) for r<=a and h(r)=(1+r^2)/((1+r)(1+ar)) for r>=a. Derivatives change sign only at r0=a/(1+sqrt(1+a^2)) and r1=sqrt(1+a^2)-a, with both values L=sqrt(2)/(1+sqrt(1+a^2)), and boundaries larger. For arbitrary unit w,z, the four signed cones spanned by w and its quarter turn provide z=alpha*epsilon*k+beta*sigma*w, alpha,beta>=0 and alpha+beta>=1; a common positive dual norm-one support for each orthogonal pair gives |f(w)|,|f(z)|>=L. The explicit pair at r0 gives equality.

## originality

PASS

Best-of-knowledge originality of the exact Baronti--Franchetti minimax value for the paper’s canonical regular octagonal plane. The defining 2014 full text supplies the definition, universal bounds, values for affine regular hexagons and ell_p^2, and octagon geometry, but nowhere evaluates Lambda(A). A 2022 same-author full paper and three distinct published exact octagonal constant records were compared by their definitions and implications; their statements do not cover the Lambda(A) optimization. Searches do not guarantee historical priority.

## value

PASS

The Baronti--Franchetti constant is a defined Banach-space geometry invariant for which exact canonical plane examples form the main mathematical study in the defining article. That same primary article introduces and analyzes the regular octagonal plane without determining this constant; the omitted exact value is therefore a natural, independently useful benchmark rather than an arbitrary slice. It lies strictly between the 1/2 and 1/sqrt(2) universal endpoints and is attained at an interior isosceles edge pair. The explicit two-branch optimization and complete all-unit-pairs reduction explain its geometric mechanism; no downstream general theorem or paper-sized contribution is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
