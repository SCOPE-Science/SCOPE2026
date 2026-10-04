from fractions import Fraction as F

# Exact algebraic witness for the first balance.
beta=F(3); b=F(2); K=F(5); Sstar=F(2)
Istar=(b*K/Sstar-b)/beta
mean_invS=F(3,5)
cov_beta_I=F(7,10)
meanI=Istar+(b*K*(mean_invS-F(1,1)/Sstar)-cov_beta_I)/beta
assert Istar == F(1)
assert meanI == F(11,10)
assert beta*meanI + cov_beta_I == b*K*mean_invS-b
assert beta*Istar == b*K/Sstar-b
assert beta*(meanI-Istar) == b*K*(mean_invS-F(1,1)/Sstar)-cov_beta_I

# Exact algebraic witness for the companion infected-growth balance,
# chosen consistently with conservation of mean population.
lamb=F(4)
Smean=F(21,10); Rstar=F(2); Rmean=F(9,5)
cov_beta_S=F(1,5); cov_lambda_R=F(3,10)
assert (Smean-Sstar)+(meanI-Istar)+(Rmean-Rstar)==0
assert beta*(Smean-Sstar)+lamb*(Rmean-Rstar)+cov_beta_S+cov_lambda_R==0

# Equality criterion is just the first identity with zero bias.
level=b*K*(mean_invS-F(1,1)/Sstar)
assert meanI==Istar if level==cov_beta_I else meanI!=Istar
print('VERIFY_OK')
