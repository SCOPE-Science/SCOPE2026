# Independent mathematical audit

## correctness

PASS

For fixed j, leafhood independently excludes j from each later parent's choices, with probability product (j−1)/(n−1). On that event, delete j and relabel in birth order. The remaining independently uniform choices give a uniform size-(n−1) recursive tree, and no surviving depth changes. The conditioning leaves D_j's mean H_(j−1) unchanged. Since the unconditional increase in expected path length is H_(n−1), this directly verifies the conditional mean shift without assuming independence of D_j and the remaining tree. Multiplying by the event probability gives the label covariance; summing by reversing the harmonic sum gives −(n−2)/4. The adjacent differences in k=j−1 are (1+H_k−H_(n−1))/(n−1), strictly increasing; harmonic integral bounds approximate the whole profile uniformly to O(1/(n−1)) by u log u at u=k/(n−1). Its unique limiting minimum is at u=1/e. The variance constants also follow directly: if v_t=Var(P_t)/t², conditioning on the size-(t−1) tree gives v_t=(1−1/t²)v_(t−1)+Var(D_t)/t², with Var(D_t)=H_(t−1)−sum_(k<t)1/k² from the depth generating function. Iteration and changing the order of the resulting nonnegative sum give lim v_t=sum_(k≥1)(1/k−1/k²)/(k+1)=2−π²/6. The leaf count grows by one minus a conditional Bernoulli with parameter L_(t−1)/(t−1), so its variance obeys w_t=(1−2/(t−1))w_(t−1)+1/4 and yields w_t=t/12 for t≥3. Thus the correlation coefficient and domain are correct. An independent hand enumeration of the six parent pairs at n=4 gave mean 13/3 and label covariances −5/18, −2/9, 0, summing to −1/2; no execution of the frozen verifier. The deterministic last label and the n=2 degeneracy agree.

## originality

PASS

The supported distinction is the fixed-birth-label conditional harmonic shift and influence profile at the frozen record, not merely its aggregate covariance or the marginal variances. There is distinct same-day exact aggregate coverage and a materially identical later indexed profile. Neither the same-day aggregate proof nor the earlier published passages gives the fixed-label profile. The catalogue comparison does not certify historical priority.

## value

PASS

The label-specific effect identifies which birth times contribute most to the negative association of two natural tree statistics. Its exact harmonic magnitude and limiting maximally negative age 1/e cannot be read from the aggregate number or its decay in correlation. This is useful even apart from the marginal asymptotics and the separate aggregate computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
